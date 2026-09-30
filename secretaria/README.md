# Secretaria

Responsabilidade editorial exclusiva de **Orion**, por acordo com Bruno. A secretaria prepara o percurso, registra avaliações e mantém continuidade. Bruno consulta os documentos e entrega atividades nas áreas do aluno.

## Documentos institucionais

- [Modelo pedagógico](modelo-pedagogico.md): organização, aula e avaliação.
- [Operação](operacao.md): criação, condução, pausa, retomada e revisões.
- [Formato dos dados](formato-dados.md): contrato dos JSONs e verificações.
- [Entrada em um Work](iniciar-work.md): instruções reutilizáveis.
- [Decisões](decisoes.md): origem das regras adotadas.
- [Catálogo](catalogo.json): cursos realmente cadastrados.

## Registros de cada curso

| Arquivo em `secretaria/cursos/<id>/` | Função |
| --- | --- |
| `curso.json` | Identidade, finalidade, escopo, pré-requisitos e ambiente |
| `curriculo.json` | Matriz versionada, sequência, objetivos e critérios |
| `estado.json` | Progresso atual, camadas trabalhadas e ponto de retomada |
| `registro.json` | Histórico de eventos e avaliações fundamentadas |

Os templates em [`templates/`](templates/README.md) não são cursos cadastrados. As ferramentas em `scripts/` instanciam esses modelos e verificam coerência; não julgam domínio do aluno.
