#!/usr/bin/env python3
"""Valida contratos e relações dos registros; não avalia aprendizagem."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERSION = "1.0.0"
LAYERS = (
    "contextualizacao", "fundamentacao", "demonstracao",
    "aplicacao", "verificacao", "consolidacao",
)
LESSON_STATES = (
    "nao_iniciada", "em_andamento", "em_verificacao", "em_reforco", "concluida",
)
EVENT_TYPES = (
    "criacao", "curriculo_aprovado", "aula_inicio", "avaliacao", "reforco",
    "aula_conclusao", "pausa", "retomada", "revisao_curriculo", "correcao",
    "curso_conclusao",
)


class ValidationError(ValueError):
    """Registro incompatível com o contrato institucional."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def string(pattern: str | None = None, choices: tuple | None = None,
           timestamp: bool = False) -> dict:
    return {"type": "string", "pattern": pattern, "choices": choices,
            "timestamp": timestamp}


def array(item: dict, minimum: int = 0) -> dict:
    return {"type": "array", "item": item, "minimum": minimum}


def obj(**fields: dict) -> dict:
    return {"type": "object", "fields": fields}


def nullable(spec: dict) -> dict:
    return {**spec, "nullable": True}


TEXT = string()
SCHEMA_VERSION = string(choices=(VERSION,))
SEMVER = string(pattern=r"\d+\.\d+\.\d+")
SLUG = string(pattern=r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*")
LESSON_ID = string(pattern=r"M\d{2,}-A\d{2,}")
TIME = string(timestamp=True)
EVAL_ID = string(pattern=r"AV\d{4,}")

CATALOG_SPEC = obj(
    versao_schema=SCHEMA_VERSION, atualizado_em=TIME,
    cursos=array(obj(id=SLUG, titulo=TEXT, pasta=TEXT, administracao=TEXT)),
)
COURSE_SPEC = obj(
    versao_schema=SCHEMA_VERSION, id=SLUG, titulo=TEXT, versao_modelo=SCHEMA_VERSION,
    criado_em=TIME, objetivo_geral=TEXT,
    escopo=obj(inclui=array(TEXT, 1), exclui=array(TEXT)),
    prerequisitos=array(TEXT), ambiente=TEXT,
)
CURRICULUM_SPEC = obj(
    versao_schema=SCHEMA_VERSION, curso_id=SLUG, versao_curriculo=SEMVER,
    situacao=string(choices=("planejamento", "vigente")),
    modulos=array(obj(
        id=string(pattern=r"M\d{2,}"), titulo=TEXT,
        aulas=array(obj(
            id=LESSON_ID, titulo=TEXT, prerequisitos=array(LESSON_ID),
            conteudos=array(TEXT, 1),
            objetivos=array(obj(id=string(pattern=r"O\d{2,}"), descricao=TEXT), 1),
            evidencia_esperada=TEXT,
            criterios=array(obj(
                id=string(pattern=r"C\d{2,}"), objetivo_id=string(pattern=r"O\d{2,}"),
                descricao=TEXT, essencial={"type": "boolean"},
            ), 1),
        ), 1),
    ), 1),
)
STATE_SPEC = obj(
    versao_schema=SCHEMA_VERSION, curso_id=SLUG, versao_curriculo=SEMVER,
    revisao={"type": "integer", "minimum": 1}, atualizado_em=TIME,
    situacao=string(choices=("planejado", "em_andamento", "pausado", "concluido")),
    aula_atual=nullable(LESSON_ID),
    aulas=array(obj(
        id=LESSON_ID, status=string(choices=LESSON_STATES),
        conteudos_apresentados=array(string(pattern=r"O\d{2,}")),
        camadas_trabalhadas=array(string(choices=LAYERS)),
        camada_atual=nullable(string(choices=LAYERS)),
        ultimo_ponto=nullable(TEXT), proxima_acao=nullable(TEXT),
        pendencias=array(TEXT), dificuldades=array(TEXT),
        ultima_avaliacao_id=nullable(EVAL_ID), concluida_em=nullable(TIME),
    ), 1),
)
RECORD_SPEC = obj(
    versao_schema=SCHEMA_VERSION, curso_id=SLUG,
    eventos=array(obj(
        id=string(pattern=r"R\d{4,}"), ocorrido_em=TIME,
        tipo=string(choices=EVENT_TYPES), descricao=TEXT,
        aula_id=nullable(LESSON_ID), avaliacao_id=nullable(EVAL_ID),
    )),
    avaliacoes=array(obj(
        id=EVAL_ID, aula_id=LESSON_ID, versao_curriculo=SEMVER,
        avaliado_em=TIME, avaliador=string(choices=("Orion",)),
        evidencia=obj(
            tipo=string(choices=("arquivo", "resposta_em_aula", "execucao")),
            referencia=nullable(TEXT),
            commit=nullable(string(pattern=r"[0-9a-f]{40}")), resumo=TEXT,
        ),
        criterios=array(obj(
            criterio_id=string(pattern=r"C\d{2,}"),
            resultado=string(choices=("nao_demonstrado", "parcial", "demonstrado")),
            justificativa=TEXT,
        ), 1),
        conclusao=string(choices=("aprovada", "reforco_necessario")), devolutiva=TEXT,
    )),
)


def parse_time(value: str) -> datetime:
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(result.tzinfo is not None, "Timestamp precisa conter fuso horário.")
    return result


def check_shape(value, spec: dict, location: str) -> None:
    if value is None and spec.get("nullable"):
        return
    kind = spec["type"]
    if kind == "object":
        require(type(value) is dict, f"{location}: objeto esperado.")
        expected = set(spec["fields"])
        require(set(value) == expected,
                f"{location}: campos ausentes {sorted(expected - set(value))}; "
                f"campos desconhecidos {sorted(set(value) - expected)}.")
        for key, child in spec["fields"].items():
            check_shape(value[key], child, f"{location}.{key}")
    elif kind == "array":
        require(type(value) is list, f"{location}: lista esperada.")
        require(len(value) >= spec["minimum"], f"{location}: lista insuficiente.")
        for index, item in enumerate(value):
            check_shape(item, spec["item"], f"{location}[{index}]")
    elif kind == "string":
        require(type(value) is str and bool(value.strip()),
                f"{location}: texto não vazio esperado.")
        if spec["pattern"]:
            require(re.fullmatch(spec["pattern"], value) is not None,
                    f"{location}: formato inválido: {value!r}.")
        if spec["choices"]:
            require(value in spec["choices"], f"{location}: valor inválido: {value!r}.")
        if spec["timestamp"]:
            try:
                parse_time(value)
            except (ValueError, TypeError) as exc:
                raise ValidationError(f"{location}: timestamp inválido: {exc}") from exc
    elif kind == "boolean":
        require(type(value) is bool, f"{location}: booleano esperado.")
    elif kind == "integer":
        require(type(value) is int and value >= spec["minimum"],
                f"{location}: inteiro >= {spec['minimum']} esperado.")
    else:
        raise ValidationError(f"Contrato desconhecido: {kind}.")


def unique(values: list, location: str) -> None:
    require(len(values) == len(set(values)), f"{location}: identificadores repetidos.")


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Chave JSON repetida: {key}.")
        result[key] = value
    return result


def load_json(path: Path, spec: dict) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
    except (OSError, ValueError) as exc:
        raise ValidationError(f"{path}: {exc}") from exc
    check_shape(data, spec, path.name)
    return data


def placeholders(value) -> bool:
    if isinstance(value, str):
        return "PREENCHER" in value or "{{" in value
    if isinstance(value, dict):
        return any(placeholders(item) for item in value.values())
    if isinstance(value, list):
        return any(placeholders(item) for item in value)
    return False


def validate_course(folder: Path, template: bool = False) -> dict:
    course = load_json(folder / "curso.json", COURSE_SPEC)
    curriculum = load_json(folder / "curriculo.json", CURRICULUM_SPEC)
    state = load_json(folder / "estado.json", STATE_SPEC)
    record = load_json(folder / "registro.json", RECORD_SPEC)
    course_id = course["id"]
    for name, data in (("curriculo", curriculum), ("estado", state), ("registro", record)):
        require(data["curso_id"] == course_id, f"{name}: curso_id divergente.")
    if not template:
        require(folder.name == course_id, "Pasta administrativa não corresponde ao curso.")
    require(state["versao_curriculo"] == curriculum["versao_curriculo"],
            "Estado não corresponde à versão do currículo.")
    planning = curriculum["situacao"] == "planejamento"
    require(not planning or state["situacao"] == "planejado",
            "Currículo em planejamento não permite iniciar aulas.")
    if not planning:
        require(not placeholders(course) and not placeholders(curriculum),
                "Curso vigente ainda contém campos PREENCHER ou placeholders.")

    module_ids = [module["id"] for module in curriculum["modulos"]]
    unique(module_ids, "Módulos")
    lessons = []
    seen = set()
    for module in curriculum["modulos"]:
        for lesson in module["aulas"]:
            lesson_id = lesson["id"]
            require(lesson_id.startswith(module["id"] + "-A"),
                    f"{lesson_id}: módulo divergente.")
            require(lesson_id not in seen, f"Aula repetida: {lesson_id}.")
            unique(lesson["prerequisitos"], f"{lesson_id}: pré-requisitos")
            require(set(lesson["prerequisitos"]) <= seen,
                    f"{lesson_id}: pré-requisito inexistente ou posterior.")
            objectives = [item["id"] for item in lesson["objetivos"]]
            criteria = [item["id"] for item in lesson["criterios"]]
            unique(objectives, f"{lesson_id}: objetivos")
            unique(criteria, f"{lesson_id}: critérios")
            require(all(item["objetivo_id"] in objectives for item in lesson["criterios"]),
                    f"{lesson_id}: critério referencia objetivo inexistente.")
            essential_targets = {
                item["objetivo_id"] for item in lesson["criterios"] if item["essencial"]
            }
            require(set(objectives) <= essential_targets,
                    f"{lesson_id}: objetivo sem critério essencial.")
            lessons.append(lesson)
            seen.add(lesson_id)

    lesson_map = {item["id"]: item for item in lessons}
    states = state["aulas"]
    require([item["id"] for item in states] == [item["id"] for item in lessons],
            "Aulas do estado não correspondem à matriz e à sua ordem.")
    evaluations = record["avaliacoes"]
    events = record["eventos"]
    unique([item["id"] for item in evaluations], "Avaliações")
    unique([item["id"] for item in events], "Eventos")
    evaluation_map = {item["id"]: item for item in evaluations}
    require(template or any(event["tipo"] == "criacao" for event in events),
            "Curso cadastrado precisa de evento de criação.")
    if state["situacao"] != "planejado":
        require(any(event["tipo"] == "curriculo_aprovado" for event in events),
                "Curso iniciado precisa de evento de aprovação curricular.")

    for event in events:
        evaluation_id = event["avaliacao_id"]
        if evaluation_id is not None:
            require(evaluation_id in evaluation_map, "Evento referencia avaliação inexistente.")
            require(event["aula_id"] == evaluation_map[evaluation_id]["aula_id"],
                    "Evento e avaliação referenciam aulas distintas.")
        if event["tipo"] == "avaliacao":
            require(evaluation_id is not None, "Evento de avaliação sem avaliação vinculada.")

    times = [parse_time(item["avaliado_em"]) for item in evaluations]
    require(times == sorted(times), "Avaliações precisam estar em ordem cronológica.")
    current_history = {}
    ordered_ids = [lesson["id"] for lesson in lessons]
    for evaluation in evaluations:
        results = evaluation["criterios"]
        unique([item["criterio_id"] for item in results], evaluation["id"])
        evidence = evaluation["evidencia"]
        if evidence["tipo"] == "arquivo":
            require(evidence["referencia"] is not None and evidence["commit"] is not None,
                    f"{evaluation['id']}: arquivo precisa de referência e commit completo.")
        require(any(event["tipo"] == "avaliacao" and
                    event["avaliacao_id"] == evaluation["id"] for event in events),
                f"{evaluation['id']}: avaliação sem evento correspondente.")
        if evaluation["versao_curriculo"] != curriculum["versao_curriculo"]:
            continue  # Histórico é preservado; só a matriz atual valida o estado.
        require(evaluation["aula_id"] in lesson_map,
                f"{evaluation['id']}: aula inexistente na matriz atual.")
        lesson = lesson_map[evaluation["aula_id"]]
        require(set(item["criterio_id"] for item in results) ==
                set(item["id"] for item in lesson["criterios"]),
                f"{evaluation['id']}: avaliação não cobre todos os critérios.")
        result_map = {item["criterio_id"]: item["resultado"] for item in results}
        essential_met = all(result_map[item["id"]] == "demonstrado"
                            for item in lesson["criterios"] if item["essencial"])
        require(essential_met == (evaluation["conclusao"] == "aprovada"),
                f"{evaluation['id']}: conclusão incompatível com os critérios essenciais.")
        if evaluation["conclusao"] == "aprovada":
            previous_ids = ordered_ids[:ordered_ids.index(evaluation["aula_id"])]
            require(all(current_history.get(previous_id) == "aprovada"
                        for previous_id in previous_ids),
                    f"{evaluation['id']}: aprovação anterior à demonstração dos pré-requisitos.")
        current_history[evaluation["aula_id"]] = evaluation["conclusao"]

    first_pending = next((item["id"] for item in states if item["status"] != "concluida"), None)
    require(state["aula_atual"] == first_pending,
            "aula_atual deve apontar à primeira aula não concluída.")
    working = [item for item in states if item["status"] not in ("nao_iniciada", "concluida")]
    require(len(working) <= 1, "Mais de uma aula em trabalho no mesmo curso.")
    previous_done = True
    for item in states:
        lesson = lesson_map[item["id"]]
        require(item["status"] in ("nao_iniciada", "concluida") or previous_done,
                f"{item['id']}: aula iniciada antes da conclusão das anteriores.")
        objectives = {objective["id"] for objective in lesson["objetivos"]}
        unique(item["conteudos_apresentados"], f"{item['id']}: conteúdos")
        unique(item["camadas_trabalhadas"], f"{item['id']}: camadas")
        require(set(item["conteudos_apresentados"]) <= objectives,
                f"{item['id']}: conteúdo referencia objetivo inexistente.")
        current_evaluations = [evaluation for evaluation in evaluations
                               if evaluation["aula_id"] == item["id"] and
                               evaluation["versao_curriculo"] == curriculum["versao_curriculo"]]
        latest = current_evaluations[-1]["id"] if current_evaluations else None
        require(item["ultima_avaliacao_id"] == latest,
                f"{item['id']}: ultima_avaliacao_id não corresponde à avaliação atual.")
        if item["status"] == "nao_iniciada":
            require(not item["conteudos_apresentados"] and not item["camadas_trabalhadas"]
                    and item["camada_atual"] is None and item["ultimo_ponto"] is None
                    and latest is None,
                    f"{item['id']}: aula não iniciada contém trabalho ou avaliação.")
        elif item["status"] != "concluida":
            require(item["ultimo_ponto"] is not None and item["proxima_acao"] is not None
                    and item["camada_atual"] is not None,
                    f"{item['id']}: aula em trabalho sem ponto e ação de retomada.")
        if item["status"] == "em_reforco":
            require(bool(item["pendencias"]), f"{item['id']}: reforço sem pendência específica.")
        if item["status"] == "concluida":
            require(latest is not None and evaluation_map[latest]["conclusao"] == "aprovada",
                    f"{item['id']}: conclusão sem avaliação aprovada atual.")
            require(item["concluida_em"] is not None and not item["pendencias"],
                    f"{item['id']}: conclusão sem data ou com pendências.")
            require(parse_time(item["concluida_em"]) >=
                    parse_time(evaluation_map[latest]["avaliado_em"]),
                    f"{item['id']}: conclusão anterior à avaliação.")
            require(any(event["tipo"] == "aula_conclusao" and
                        event["aula_id"] == item["id"] and
                        event["avaliacao_id"] == latest for event in events),
                    f"{item['id']}: conclusão sem evento fundamentado.")
        else:
            require(item["concluida_em"] is None,
                    f"{item['id']}: aula não concluída contém data de conclusão.")
        previous_done = previous_done and item["status"] == "concluida"

    if state["situacao"] == "planejado":
        require(all(item["status"] == "nao_iniciada" for item in states) and not evaluations,
                "Curso planejado contém aulas iniciadas ou avaliações.")
    require((first_pending is None) == (state["situacao"] == "concluido"),
            "Situação do curso não corresponde à conclusão de suas aulas.")
    if state["situacao"] == "concluido":
        require(any(event["tipo"] == "curso_conclusao" for event in events),
                "Curso concluído sem evento de conclusão.")
    return course


def validate_repo(root: Path) -> list[str]:
    errors = []
    try:
        validate_course(root / "secretaria/templates/administracao", template=True)
    except ValidationError as exc:
        errors.append(f"Template: {exc}")
    try:
        catalog = load_json(root / "secretaria/catalogo.json", CATALOG_SPEC)
        unique([item["id"] for item in catalog["cursos"]], "Catálogo")
    except ValidationError as exc:
        return errors + [f"Catálogo: {exc}"]
    ids = {item["id"] for item in catalog["cursos"]}
    for base in (root / "cursos", root / "secretaria/cursos"):
        if not base.is_dir():
            errors.append(f"Pasta obrigatória ausente: {base}")
            continue
        for folder in base.iterdir():
            if folder.is_dir() and not folder.name.startswith(".") and folder.name not in ids:
                errors.append(f"Pasta de curso fora do catálogo: {folder}")
    for entry in catalog["cursos"]:
        try:
            course_id = entry["id"]
            require(entry["pasta"] == f"cursos/{course_id}" and
                    entry["administracao"] == f"secretaria/cursos/{course_id}",
                    "Caminhos do catálogo divergentes do identificador.")
            materials = root / entry["pasta"]
            require(materials.is_dir() and (materials / "README.md").is_file(),
                    "Pasta de materiais ou README ausente.")
            course = validate_course(root / entry["administracao"])
            require(course["titulo"] == entry["titulo"], "Título divergente do catálogo.")
        except ValidationError as exc:
            errors.append(f"{entry['id']}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Raiz do repositório.")
    args = parser.parse_args()
    errors = validate_repo(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 1
    print("Registros válidos: contratos, versões, sequência e evidências referenciadas.")
    print("A validação estrutural não substitui a avaliação pedagógica de Orion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
