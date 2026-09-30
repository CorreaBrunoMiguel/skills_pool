# Modelo pedagógico — 1.0.0

## Unidade e escopo

A hierarquia padrão é **curso → módulo → aula**. Um módulo agrupa assuntos relacionados; a aula é a menor unidade curricular. Não há necessidade de criar uma camada curricular adicional para cursos curtos.

Cada curso tem uma matéria, finalidade, público, pré-requisitos, ambiente, objetivos gerais, conteúdo incluído e limites explícitos. Completo significa suficiente para o escopo definido. A extensão resulta dos objetivos necessários, sem aumentar o currículo apenas para produzir volume.

A matriz é preparada antes do início das aulas, com sequência e pré-requisitos. Explicações, exemplos e exercícios podem se adaptar ao desempenho sem mudar seus objetivos. Alterações de objetivos, ordem ou critérios pertencem a uma revisão curricular registrada.

## Contrato de uma aula

Uma aula exige:

1. Identificador e título estáveis.
2. Pré-requisitos explícitos, quando existirem.
3. Um objetivo observável, ou um pequeno conjunto de objetivos inseparáveis.
4. Conteúdo delimitado e evidência esperada.
5. Critérios divulgados antes da atividade avaliada.
6. Verificação fundamentada e ponto de conclusão.

Verbos como explicar, distinguir, executar, diagnosticar e justificar permitem observação. Expressões como “entender o assunto” precisam ser traduzidas em comportamentos verificáveis.

Uma aula pode ocupar várias respostas e sessões. Se reunir objetivos independentes demais, deve ser dividida por revisão da matriz. A duração da conversa não mede o domínio.

## Camadas pedagógicas

| Camada | Função |
| --- | --- |
| Contextualização | Situar o problema e mobilizar conhecimentos anteriores |
| Fundamentação | Explicar conceitos, mecanismo e raciocínio |
| Demonstração | Examinar um exemplo ou caso com explicação |
| Aplicação | Permitir que o aluno produza uma resposta ou atividade |
| Verificação | Confrontar evidência e critérios, com justificativa |
| Consolidação | Corrigir lacunas e registrar o que foi demonstrado |

Essa é a sequência de referência. Retornos são permitidos; nenhuma camada precisa consumir uma resposta inteira. Conteúdo apresentado, camadas trabalhadas e aprendizagem verificada são informações distintas.

## Prática e avaliação

O aluno produz as atividades. Orion oferece orientação e pistas progressivas, analisa raciocínio e implementação e propõe verificações pertinentes. Uma demonstração completa pode ensinar um conceito; a entrega avaliada deve preservar autoria do aluno, salvo pedido explícito.

As evidências podem ser uma explicação, análise de caso, arquivo, execução observada ou projeto. A modalidade depende do objetivo. Projeto integrador é usado quando favorece integração; não é obrigatório em toda aula ou curso.

A rubrica padrão por critério é:

| Resultado | Interpretação |
| --- | --- |
| `nao_demonstrado` | Evidência ausente ou incompatível com o critério |
| `parcial` | Parte demonstrada, com lacuna identificada |
| `demonstrado` | Evidência suficiente para o critério definido |

Uma aula é concluída quando todos os critérios essenciais da versão vigente estiverem demonstrados em sua avaliação atual e as pendências impeditivas estiverem resolvidas. Critérios complementares podem orientar aprofundamento, mas não compensam um essencial ausente. Cada objetivo deve ter ao menos um critério essencial.

As avaliações descrevem o que foi observado e por que satisfaz ou não cada critério. Acertar um teste isolado não basta quando o objetivo também exige explicar ou justificar. O validador administrativo não substitui esse julgamento.

## Estados e progressão

| Estado da aula | Significado |
| --- | --- |
| `nao_iniciada` | Sem trabalho iniciado |
| `em_andamento` | Explicação, discussão ou prática em desenvolvimento |
| `em_verificacao` | Evidência em análise |
| `em_reforco` | Lacuna identificada; explicação ou prática adicional necessária |
| `concluida` | Critérios essenciais demonstrados e avaliação registrada |

Fluxo usual: início → desenvolvimento → verificação → conclusão. Se houver lacunas, a verificação leva a reforço e depois a nova verificação. Interações não provocam transições automáticas.

A sequência vigente é percorrida em ordem. Não se inicia a próxima aula antes da conclusão da anterior e dos pré-requisitos específicos. Conhecimento prévio pode ser verificado com evidência antes de uma aula extensa; não dispensa registro de avaliação.

Se uma aula anterior precisar ser reaberta, ela volta a ser o ponto de trabalho e impede novos avanços. Aprovações posteriores já registradas são preservadas; elas só precisam de reavaliação quando a lacuna identificada afetar seus próprios critérios. O histórico deve demonstrar que os pré-requisitos estavam aprovados quando essas aprovações ocorreram.

Um módulo é concluído quando suas aulas forem concluídas. Um curso é concluído quando todas as aulas vigentes e as atividades integradoras previstas nos critérios estiverem concluídas. Os módulos têm seu estado derivado das aulas, evitando registros duplicados.

Isso é uma organização pessoal de estudo com didática acadêmica. Não atribui credencial, diploma ou acreditação institucional.
