# Templates

Estes arquivos são modelos para instanciar cursos. Não representam um curso iniciado nem uma avaliação real.

- `administracao/`: quatro JSONs com estrutura válida e marcadores `PREENCHER`.
- `curso/`: materiais e áreas de trabalho que serão copiados para `cursos/<id>/`.

Orion pode executar `python secretaria/scripts/novo_curso.py --id <id> --titulo "<título>"`. O comando cria pastas, registra a entrada no catálogo e verifica consistência. Não publica no GitHub, não finaliza o currículo e não inicia a aula.

Depois da instanciação, Orion substitui os marcadores, amplia a matriz para cobrir o escopo e atualiza o estado com as mesmas aulas. Só então declara a matriz vigente. Não é preciso preencher todos os materiais de aula antecipadamente.
