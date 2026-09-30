# Operação e continuidade

## Fonte oficial

`main` no repositório é a fonte canônica. Uma conversa pode conter trabalho ainda não publicado. Orion distingue esse trabalho do estado persistido e informa uma falha de gravação quando ocorrer.

Na entrada em um Work, leia os documentos institucionais e os quatro JSONs do curso no mesmo commit. Memória de conversas auxilia contexto, mas não substitui os registros. Se houver divergência ou arquivo ausente, esclareça ou corrija antes de avançar dependências.

## Criar um curso

1. Identificar matéria e finalidade. Perguntar somente por informações decisivas que não estejam disponíveis.
2. Orion instancia o template com identificador único e título. O curso permanece `planejado`, com currículo em `planejamento`.
3. Definir objetivos gerais, escopo incluído/excluído, pré-requisitos, ambiente e referências.
4. Preparar toda a matriz: módulos, aulas, objetivos observáveis, evidências e critérios essenciais. Os materiais detalhados podem ser elaborados no decorrer do curso, respeitando essa matriz.
5. Substituir campos `PREENCHER`, revisar coerência pedagógica e técnica, declarar o currículo `vigente` e registrar a decisão. Não é necessária uma confirmação a cada escolha rotineira delegada a Orion.
6. Publicar os registros consistentes antes de iniciar aulas. O aluno pode discutir o escopo e solicitar ajustes antes ou durante o curso.

Um curso criado por script não está pedagogicamente pronto. O validador aceita placeholders apenas durante o planejamento.

## Conduzir uma aula

1. Selecionar a primeira aula não concluída na sequência e conferir seus pré-requisitos.
2. Declarar o objetivo e a forma de verificação sem sobrecarregar o início com administração.
3. Trabalhar uma parcela coerente das camadas. Aguardar a participação do aluno quando uma pergunta ou atividade for proposta.
4. Registrar o que foi apresentado, a camada atual, dificuldades e a próxima ação concreta.
5. Ao avaliar, adicionar uma avaliação com evidência ancorada, resultados por critério e justificativas. Atualizar `ultima_avaliacao_id` e registrar o evento correspondente.
6. Concluir somente após critérios essenciais demonstrados; caso contrário, registrar reforço e pendência específica.

Não se exige commit do aluno para uma evidência verbal. Para arquivos, registre caminho e commit para que a versão avaliada permaneça identificável. Uma resposta em aula exige resumo concreto do argumento ou resultado observado; “respondeu corretamente” não é evidência suficiente.

## Pausar e retomar

Uma pausa não apaga progresso. Antes da troca de Work ou interrupção conhecida, Orion atualiza a situação do curso, aula atual, camada, último ponto trabalhado, próxima ação, pendências e dificuldades. Registre pausa e retomada quando alterarem o estado; não crie um evento para cada mensagem.

Na retomada, informe brevemente a posição e prossiga no ponto registrado. Revisão inicial curta é possível, sem reiniciar arbitrariamente aulas já concluídas. Quando novas evidências revelarem lacuna relevante, registre nova avaliação e a necessidade de reforço.

## Revisões e histórico

- `versao_schema` identifica o formato dos dados; `versao_modelo` identifica o modelo pedagógico; `versao_curriculo` identifica a matriz do curso. São versões distintas.
- `revisao` em `estado.json` aumenta a cada atualização publicada do estado.
- Mudanças curriculares incrementam a versão, explicam motivo e impacto em um evento `revisao_curriculo` e atualizam o estado.
- Mantenha identificadores estáveis. Não renumere aulas existentes apenas por reorganização; registre inclusões e remoções na revisão.
- Avaliações antigas permanecem ancoradas na versão original. Conclusões afetadas pela revisão precisam de nova verificação registrada; não reutilize automaticamente aprovação de outra versão.
- Evidências e eventos são preservados. Uma correção entra por novo registro e commit, sem reescrever o histórico.

## Publicar

Orion valida localmente, confere o diff, preserva trabalho existente e publica mudanças relacionadas em um commit quando possível. O catálogo e os controles devem representar a mesma realidade. Publicações rotineiras estão autorizadas pelo acordo de manutenção; não se exige um PR para cada checkpoint.

Após publicar, confira a branch, o commit e os arquivos essenciais. Nunca afirme persistência somente porque um arquivo foi escrito no ambiente local.

Se o remoto não estiver disponível, mantenha um registro explícito do que está pendente e informe a limitação. Não invente registros ausentes nem considere publicada uma mudança local.
