# Contrato dos dados — 1.0.0

Os JSONs são UTF-8, com indentação de dois espaços. Todos usam `versao_schema: "1.0.0"`. Campos obrigatórios e tipos são verificados por `scripts/validar.py`; esse script é a definição executável do formato. Os templates mostram exemplos completos.

## Catálogo

`catalogo.json` contém `versao_schema`, `atualizado_em` e `cursos`. Cada entrada contém `id`, `titulo`, `pasta` e `administracao`. Os caminhos são derivados do identificador e devem corresponder às pastas reais. Templates não são cadastrados.

O identificador do curso usa letras minúsculas, números e hífens, começando por letra. Uma entrada tem caminhos `cursos/<id>` e `secretaria/cursos/<id>`.

## Identidade e matriz

`curso.json` contém identidade, modelo, data de criação, objetivo geral, escopo incluído/excluído, pré-requisitos e ambiente.

`curriculo.json` contém curso, versão, situação (`planejamento` ou `vigente`), módulos e aulas. Cada aula contém:

- `id`, `titulo`, `prerequisitos` e `conteudos`;
- `objetivos`: identificador e descrição observável;
- `evidencia_esperada`: produto ou resposta que será verificado;
- `criterios`: identificador, objetivo relacionado, descrição e indicador `essencial`.

Módulos usam `M01`, `M02` etc.; aulas usam `M01-A01`, `M01-A02` etc. A ordem das listas define o percurso. Objetivos (`O01`) e critérios (`C01`) são únicos dentro da aula. Pré-requisitos referem-se a aulas anteriores; cada objetivo exige um critério essencial.

## Estado

`estado.json` contém curso, versão do currículo, revisão, data, situação (`planejado`, `em_andamento`, `pausado` ou `concluido`), `aula_atual` e lista de aulas.

Cada aula registra `status`, `conteudos_apresentados`, `camadas_trabalhadas`, `camada_atual`, `ultimo_ponto`, `proxima_acao`, `pendencias`, `dificuldades`, `ultima_avaliacao_id` e `concluida_em`.

- `conteudos_apresentados` referencia objetivos cujo conteúdo foi apresentado, sem alegar domínio.
- Camadas usam os nomes do modelo em minúsculas, sem acentos.
- Campos ainda inexistentes usam `null`, em vez de uma aprovação fictícia.
- Pendências são impeditivos atuais; dificuldades podem preservar observações já superadas.
- Só existe uma aula em trabalho por curso. A aula seguinte exige conclusão das anteriores.
- Uma reabertura pode coexistir com aulas posteriores já concluídas; o histórico deve comprovar a sequência original. O trabalho retorna à primeira pendência e novos avanços ficam bloqueados.
- `aula_atual` aponta para a primeira aula não concluída; pode estar ainda não iniciada. Um curso concluído usa `null`.

## Registro

`registro.json` contém curso, `eventos` e `avaliacoes`.

Eventos têm `id`, `ocorrido_em`, `tipo`, `descricao`, `aula_id` opcional (`null` para evento geral) e `avaliacao_id` opcional. Tipos: `criacao`, `curriculo_aprovado`, `aula_inicio`, `avaliacao`, `reforco`, `aula_conclusao`, `pausa`, `retomada`, `revisao_curriculo`, `correcao` e `curso_conclusao`.

Avaliações têm `id`, `aula_id`, `versao_curriculo`, `avaliado_em`, `avaliador`, `evidencia`, `criterios`, `conclusao` e `devolutiva`.

Uma evidência possui `tipo`, `referencia`, `commit` e `resumo`. Tipos: `arquivo`, `resposta_em_aula`, `execucao`. Para `arquivo`, referência e SHA completo de commit são obrigatórios. Para respostas e execuções observadas, o resumo deve permitir compreender o que foi demonstrado. Uma execução apoiada em código versionado também pode ter referência e commit.

Cada resultado por critério tem `criterio_id`, `resultado` (`nao_demonstrado`, `parcial`, `demonstrado`) e `justificativa`. A conclusão é `aprovada` ou `reforco_necessario`. `aprovada` exige todos os essenciais demonstrados. A avaliação atual deve cobrir todos os critérios da aula.

## Garantias e limites

O validador verifica tipos, campos, referências, versões, sequência, critérios, avaliações e conclusão. Avaliações de versões anteriores são preservadas, mas não validam o estado da matriz atual.

A ferramenta não comprova autenticidade, não executa o trabalho avaliado e não decide se a justificativa é pedagogicamente suficiente. Orion continua responsável por ler a evidência e aplicar os critérios. O histórico Git permite consultar matrizes anteriores.
