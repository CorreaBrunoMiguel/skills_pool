# Bash — do básico ao avançado

Matriz vigente **1.0.0**: 10 módulos, 40 aulas. Sem carga horária fixa; progressão por aprendizagem demonstrada.

Objetivo: usar Bash no Linux com autonomia e criar automações legíveis, verificáveis e robustas. Bruno implementa as atividades; Orion ensina, revisa, avalia e mantém os registros.

## Como acompanhar as aulas

A aula acontece nesta conversa. Orion apresenta o objetivo, ensina um bloco coerente, demonstra com exemplos e dá espaço para perguntas. Depois propõe uma prática ou verificação compatível com o que foi ensinado. Uma aula pode ocupar várias mensagens e sessões.

- Os arquivos em `aulas/` são materiais de apoio e revisão; sua existência não implica leitura prévia obrigatória.
- Quando houver leitura preparatória, Orion informa explicitamente o arquivo ou trecho, o objetivo da leitura e o que fazer depois.
- Perguntas de sondagem identificam o ponto de partida. Discussão e dúvidas durante a explicação não equivalem automaticamente a avaliação formal.
- Antes de uma atividade avaliada, Orion indica que é uma verificação e informa evidência e critérios. Não exige uma formulação decorada; considera o raciocínio demonstrado.
- Bruno responde, pergunta e realiza as práticas solicitadas. Não precisa atualizar secretaria, currículo ou estado.
- Orion mantém os registros em pontos relevantes de aprendizagem e informa a conclusão da aula. Um “ok” permite continuar a conversa, mas não comprova domínio nem conclui a aula.

## Matriz curricular

| Módulo | Conteúdo | Aulas |
| --- | --- | --- |
| M01 | Fundamentos do shell e do sistema de arquivos | 4 |
| M02 | Interpretação de comandos e expansões | 4 |
| M03 | Fluxos e processamento de texto | 4 |
| M04 | Programação de scripts | 4 |
| M05 | Estruturação e recursos de Bash | 4 |
| M06 | Automação de arquivos e integração | 4 |
| M07 | Falhas, limpeza e execução previsível | 4 |
| M08 | Processos e recursos avançados | 4 |
| M09 | Qualidade, portabilidade e operação | 4 |
| M10 | Projeto integrador de automação | 4 |

## Aulas e critérios

A sequência é obrigatória. Cada aula combina explicação, demonstração, aplicação e verificação; pode ocupar várias sessões. Todos os critérios essenciais precisam ser demonstrados. Conhecimento prévio será verificado antes de encurtar uma aula.

### M01 — Fundamentos do shell e do sistema de arquivos

- **M01-A01 — Terminal, shell e Bash**: Distinguir terminal, shell, Bash e programa executado, identificando o interpretador usado.
- **M01-A02 — Navegação e caminhos**: Navegar no sistema de arquivos e resolver caminhos a partir do diretório atual.
- **M01-A03 — Arquivos, diretórios e links**: Manipular arquivos e diretórios de laboratório, explicando os efeitos sobre links.
- **M01-A04 — Permissões e resolução de comandos**: Diagnosticar permissão de acesso e resolução de um comando.
### M02 — Interpretação de comandos e expansões

- **M02-A01 — Argumentos, aspas e escapes**: Prever os argumentos produzidos por uma linha de comando com aspas e escapes.
- **M02-A02 — Variáveis e ambiente**: Explicar e verificar o alcance de uma variável no shell e em um processo filho.
- **M02-A03 — Globbing e ordem das expansões**: Prever expansões e impedir divisão ou expansão de nomes indesejada.
- **M02-A04 — Status de saída e composição**: Controlar execução pela condição de sucesso ou falha de comandos.
### M03 — Fluxos e processamento de texto

- **M03-A01 — Redirecionamentos e pipelines**: Construir um fluxo separando dados e diagnósticos e prever seus destinos.
- **M03-A02 — Busca e expressões regulares**: Selecionar linhas com busca literal e padrões regulares compatíveis com a tarefa.
- **M03-A03 — Transformação e agregação de texto**: Transformar e agregar texto delimitado com hipóteses de formato explícitas.
- **M03-A04 — AWK para registros e campos**: Produzir um resumo de registros com filtros e agregações em AWK.
### M04 — Programação de scripts

- **M04-A01 — Criação e execução de scripts**: Criar e executar um script identificando seu interpretador e modos de invocação.
- **M04-A02 — Entrada e argumentos**: Receber argumentos e entrada textual preservando valores e validando o contrato.
- **M04-A03 — Condições e seleção**: Selecionar comportamentos por condições com a sintaxe adequada ao tipo de dado.
- **M04-A04 — Repetição e leitura de registros**: Percorrer argumentos e registros preservando seus limites.
### M05 — Estruturação e recursos de Bash

- **M05-A01 — Funções e escopo**: Decompor um script em funções com contratos explícitos.
- **M05-A02 — Expansão de parâmetros e aritmética**: Transformar valores e calcular inteiros usando recursos do Bash.
- **M05-A03 — Arrays indexados e associativos**: Representar e percorrer coleções preservando cada elemento.
- **M05-A04 — Configuração e contratos de interface**: Projetar a interface de um script com configuração previsível e dados não executáveis.
### M06 — Automação de arquivos e integração

- **M06-A01 — Busca e processamento de nomes**: Processar conjuntos de arquivos preservando integralmente seus nomes.
- **M06-A02 — Arquivamento e integridade**: Criar e verificar um arquivo de backup e demonstrar sua restauração.
- **M06-A03 — Bash em fluxos de dados**: Orquestrar ferramentas adequadas a cada formato de dados.
- **M06-A04 — Integração com serviços e comandos externos**: Orquestrar uma operação externa com resultados e falhas explícitos.
### M07 — Falhas, limpeza e execução previsível

- **M07-A01 — Tratamento explícito de falhas**: Projetar o caminho de falha de um script sem depender de suposições sobre opções do shell.
- **M07-A02 — Sinais, traps e temporários**: Gerenciar recursos temporários e encerramento em sucesso, falha e interrupção.
- **M07-A03 — Idempotência e gravação consistente**: Executar uma transformação repetidamente sem corromper a saída.
- **M07-A04 — Logs e observabilidade**: Produzir dados e diagnósticos que permitam investigar uma execução.
### M08 — Processos e recursos avançados

- **M08-A01 — Processos e controle de jobs**: Iniciar, acompanhar e aguardar processos com status verificável.
- **M08-A02 — Subshells e substituições**: Prever alterações de estado e fluxos em diferentes contextos de execução.
- **M08-A03 — Descritores e entrada multilinha**: Construir entrada multilinha e manipular descritores com expansão controlada.
- **M08-A04 — Concorrência e exclusão mútua**: Executar tarefas concorrentes com limite e proteção de um recurso compartilhado.
### M09 — Qualidade, portabilidade e operação

- **M09-A01 — Depuração e análise estática**: Localizar e explicar defeitos sintáticos e de interpretação em scripts.
- **M09-A02 — Testes de comportamento**: Verificar o contrato de um script por cenários reproduzíveis.
- **M09-A03 — Compatibilidade e desempenho**: Avaliar a compatibilidade e o custo de execução de uma solução.
- **M09-A04 — Execução não interativa e agendamento**: Preparar uma automação para execução não interativa previsível.
### M10 — Projeto integrador de automação

- **M10-A01 — Requisitos e desenho**: Definir um contrato verificável para a automação integradora.
- **M10-A02 — Implementação modular**: Implementar o contrato do projeto com organização e efeitos controlados.
- **M10-A03 — Verificação e correção**: Demonstrar comportamento correto e corrigir defeitos com evidência.
- **M10-A04 — Entrega e defesa técnica**: Entregar e defender uma automação reproduzível com limites explícitos.

## Registros oficiais

- [Identidade e escopo](../../secretaria/cursos/bash/curso.json)
- [Currículo e critérios por aula](../../secretaria/cursos/bash/curriculo.json)
- [Estado e ponto de retomada](../../secretaria/cursos/bash/estado.json)
- [Histórico de eventos e avaliações](../../secretaria/cursos/bash/registro.json)
- [Referências](referencias.md)

## Ambiente e entregas

Usaremos o Linux Mint informado por Bruno. O diagnóstico local da primeira aula identificou Bash ativo e versão instalada 5.1.16(1)-release. As atividades manipulam somente fixtures em pasta de laboratório. Não é necessário instalar nada antes do diagnóstico. Código avaliado fica em `atividades/<aula-id>/`; projeto final em `projetos/automacao-arquivos/`. A origem dos arquivos avaliados será registrada por commit.

## Projeto integrador

Bruno construirá uma ferramenta de inventário e backup de arquivos de laboratório, com CLI, resultados verificáveis, logs, tratamento de falhas e testes. O contrato detalhado será produzido por Bruno em M10-A01 e revisado por Orion antes da implementação.
