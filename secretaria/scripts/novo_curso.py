#!/usr/bin/env python3
"""Instancia um curso em planejamento; não inicia aulas nem publica no GitHub."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from validar import ROOT, validate_repo


def write_json(path: Path, data: dict) -> None:
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                         encoding="utf-8")
    temporary.replace(path)


def create_course(root: Path, course_id: str, title: str) -> None:
    if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", course_id):
        raise ValueError("Identificador deve usar letras minúsculas, números e hífens.")
    if not title.strip() or "\n" in title or "\r" in title:
        raise ValueError("Título deve ser um texto não vazio em uma linha.")
    title = title.strip()
    errors = validate_repo(root)
    if errors:
        raise ValueError("Corrija o repositório antes de instanciar: " + "; ".join(errors))
    catalog_path = root / "secretaria/catalogo.json"
    original = catalog_path.read_bytes()
    catalog = json.loads(original)
    if any(entry["id"] == course_id for entry in catalog["cursos"]):
        raise ValueError(f"Curso já cadastrado: {course_id}.")
    materials = root / "cursos" / course_id
    administration = root / "secretaria/cursos" / course_id
    if materials.exists() or administration.exists():
        raise ValueError("Uma das pastas de destino já existe; nada foi alterado.")
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        shutil.copytree(root / "secretaria/templates/curso", materials)
        shutil.copytree(root / "secretaria/templates/administracao", administration)
        for path in materials.rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            content = content.replace("{{CURSO_ID}}", course_id).replace("{{TITULO}}", title)
            path.write_text(content, encoding="utf-8")
        for filename in ("curso.json", "curriculo.json", "estado.json", "registro.json"):
            path = administration / filename
            data = json.loads(path.read_text(encoding="utf-8"))
            if filename == "curso.json":
                data.update(id=course_id, titulo=title, criado_em=now)
            else:
                data["curso_id"] = course_id
            if filename == "estado.json":
                data["atualizado_em"] = now
            elif filename == "registro.json":
                data["eventos"] = [{
                    "id": "R0001", "ocorrido_em": now, "tipo": "criacao",
                    "descricao": "Curso instanciado em planejamento; matriz ainda não vigente.",
                    "aula_id": None, "avaliacao_id": None,
                }]
            write_json(path, data)
        catalog["cursos"].append({
            "id": course_id, "titulo": title,
            "pasta": f"cursos/{course_id}",
            "administracao": f"secretaria/cursos/{course_id}",
        })
        catalog["atualizado_em"] = now
        write_json(catalog_path, catalog)
        errors = validate_repo(root)
        if errors:
            raise ValueError("Instanciação inconsistente: " + "; ".join(errors))
    except Exception:
        catalog_path.write_bytes(original)
        if materials.exists():
            shutil.rmtree(materials)
        if administration.exists():
            shutil.rmtree(administration)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True, help="Identificador único, por exemplo bash.")
    parser.add_argument("--titulo", required=True, help="Título do curso.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Raiz do repositório.")
    args = parser.parse_args()
    try:
        create_course(args.root.resolve(), args.id, args.titulo)
    except (OSError, ValueError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1
    print(f"Curso {args.id!r} criado em planejamento. Nenhuma aula foi iniciada.")
    print("Orion deve preencher escopo e matriz, validar e publicar os registros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
