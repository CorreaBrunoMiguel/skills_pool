# Skills Pool

Instituição de estudo organizada em cursos de uma matéria específica, com currículo definido, aulas progressivas, prática autoral e aprendizagem verificada.

**Orion** coordena currículo, docência, avaliações, secretaria e continuidade. **Bruno** estuda, discute, implementa as atividades e apresenta evidências. A responsabilidade editorial da secretaria é exclusivamente de Orion, por acordo entre os participantes; isso não constitui uma restrição técnica de acesso.

## Organização

| Local | Função | Responsável editorial |
| --- | --- | --- |
| [`secretaria/`](secretaria/README.md) | Normas, catálogo, templates, controles e ferramentas administrativas | Orion |
| [`secretaria/cursos/`](secretaria/cursos/README.md) | Currículo e registros oficiais de cada curso | Orion |
| [`cursos/`](cursos/README.md) | Aulas, referências, atividades e projetos | Orion nos materiais; Bruno nas entregas |
| [`AGENTS.md`](AGENTS.md) | Instruções para agentes que iniciam ou retomam o trabalho | Orion |

Cada curso recebe uma pasta em `cursos/<curso-id>/` e uma pasta administrativa correspondente em `secretaria/cursos/<curso-id>/`.

## Modelo de aprendizagem

**Curso → módulo → aula.** A aula é a menor unidade curricular, com objetivo delimitado, evidência verificável e critério de conclusão. Camadas pedagógicas organizam a aula; prompts e respostas são interações dentro dela. Uma aula pode ocupar várias sessões.

Conteúdo apresentado e aprendizagem demonstrada são registrados separadamente. A sequência curricular é definida antes da primeira aula; adaptações didáticas não alteram a matriz. Mudanças curriculares têm justificativa e versão.

## Início e continuidade

1. Consultar o [catálogo](secretaria/catalogo.json).
2. Para iniciar uma matéria, definir seu escopo e preparar a matriz com Orion.
3. Para retomar, usar as [instruções de entrada em um Work](secretaria/iniciar-work.md).

O estado oficial é o publicado na branch `main`. Em uma sessão, Orion atualiza os registros necessários e informa quando a persistência foi concluída. Acesso ao GitHub deve estar disponível; a conversa, sozinha, não atualiza o repositório.

## Ferramentas administrativas

Requerem Python 3.10 ou superior, sem dependências externas.

```bash
python secretaria/scripts/validar.py
python secretaria/scripts/novo_curso.py --id bash --titulo "Bash"
```

O segundo comando cria um curso **em planejamento**, com campos a preencher. Criar pastas não aprova o currículo nem inicia aulas. Orion executa essas ferramentas como parte da administração.

## Estado inicial

Modelo institucional: **1.0.0**. Nenhum curso foi iniciado ou migrado. Bash, Git e Docker são exemplos de matérias possíveis.
