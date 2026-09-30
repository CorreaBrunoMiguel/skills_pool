# Decisões institucionais

Data de implantação: **2026-09-30**. Modelo: **1.0.0**.

## Diretrizes estabelecidas com Bruno

| ID | Decisão | Origem |
| --- | --- | --- |
| D001 | Modelo reutilizável para cursos de matérias específicas | Definição do usuário |
| D002 | Aula é a menor unidade curricular, mensurável e verificável; pode ocupar várias interações | Definição do usuário |
| D003 | Aulas têm camadas pedagógicas internas | Definição do usuário |
| D004 | Cada curso tem matriz pré-determinada e segue seu percurso | Definição do usuário |
| D005 | Monorepo preserva alinhamento e continuidade entre Works | Escolha discutida e autorizada |
| D006 | Orion assume docência, currículo, avaliação e administração | Delegação explícita do usuário |
| D007 | Secretaria tem responsabilidade editorial exclusiva de Orion, por acordo | Delegação explícita do usuário |
| D008 | Bruno é aluno e autor das atividades; Orion mantém os controles | Divisão estabelecida na conversa |
| D009 | Orion pode criar, modificar e organizar o skills_pool | Autorização explícita de manutenção |

## Escolhas operacionais de Orion nesta implantação

| ID | Escolha | Motivo |
| --- | --- | --- |
| O001 | `secretaria/` e `cursos/` na raiz; administração de cada curso dentro da secretaria | Separar responsabilidade editorial e entregas |
| O002 | Hierarquia curso → módulo → aula | Evitar divisões redundantes em cursos curtos |
| O003 | Markdown, JSON e Python sem dependências externas | Leitura humana, dados estruturados e portabilidade |
| O004 | Main como fonte canônica; mudanças normais em commits | Continuidade e histórico auditável |
| O005 | Rubrica por critério e avaliação com evidência ancorada | Medir aprendizagem sem aprovação por simples exposição |
| O006 | Catálogo inicialmente vazio | Não criar matérias ou migrar cursos sem solicitação |
| O007 | Respeitar a visibilidade pública encontrada no repositório | Manutenção do repositório fornecido sem alterar configurações |

Novas decisões relevantes recebem novas entradas. Correções e revisões indicam o que mudou e por quê; não alteram silenciosamente a origem de uma regra.
