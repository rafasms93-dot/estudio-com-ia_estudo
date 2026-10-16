# AGENTS.md · Contrato operacional da RFL Agency

Este arquivo é o contrato global de governança para qualquer IA, agente ou runtime que trabalhe dentro da RFL Agency.

## 1. Identidade e cadeia de autoridade

A RFL Agency é uma empresa AI-native de uma pessoa.

1. **Rafael é o Diretor.** Define intenção, prioridade, critérios de aceite e decisão final.
2. **R.A.Q.U.E.L. é a camada de orquestração.** Interpreta pedidos, encontra contexto, roteia trabalho e mantém continuidade.
3. **MARK é o sistema operacional institucional.** Guarda estado, regras, projetos, decisões, histórico, prioridades e checkpoints.
4. **Agentes, modelos, MCPs, runtimes e ferramentas executam.** Eles não governam a empresa e não substituem as fontes de verdade.

Nunca obrigue o Diretor a procurar manualmente uma pasta, reconstruir contexto ou escolher uma ferramenta quando o sistema puder descobrir isso.

## 2. Regra central de operação

Todo pedido segue este fluxo:

```text
ENTRADA → CLASSIFICAR → ROTEAR → CARREGAR CONTEXTO → EXECUTAR → VALIDAR → PERSISTIR
```

A conversa é ambiente temporário de trabalho. Informação institucional relevante deve terminar na fonte de verdade correta.

## 3. Antes de executar qualquer tarefa

1. Leia `CORE/AGENCY.md`.
2. Leia `CORE/ROUTER.md`.
3. Classifique o pedido por natureza, unidade, projeto e estado.
4. Carregue **somente o contexto mínimo suficiente**.
5. Identifique a fonte de verdade antes de escrever.
6. Só então execute.

Não carregue toda a empresa para responder uma tarefa local. Contexto excessivo aumenta custo, mistura projetos e piora decisões.

## 4. Fontes de verdade

| Tipo | Fonte preferencial |
|---|---|
| Operação, decisões, processos, status, gestão | Notion |
| Planilhas, dados estruturados, arquivos compartilhados | Google Drive / Sheets |
| Código, contratos operacionais, runtime, automação | GitHub |
| Produção local pesada | Workstation |
| Arquitetura visual | Miro |

Miro é mapa, não banco de estado. Filesystem também não deve ser tratado como banco de estado quando já existe uma fonte operacional superior.

## 5. Projetos MARK

Projetos MARK devem permanecer rasos e previsíveis. Estrutura canônica:

```text
PROJECT.md
CANON.md
STATE.md
CHECKPOINT.md
ASSETS/
PRODUCTION/
OUTPUTS/
DOCS/
ARCHIVE/
```

- `PROJECT.md`: propósito, escopo e definição do projeto.
- `CANON.md`: decisões e regras canônicas.
- `STATE.md`: estado operacional atual.
- `CHECKPOINT.md`: último ponto seguro de retomada.
- `ASSETS/`: insumos.
- `PRODUCTION/`: trabalho em andamento.
- `OUTPUTS/`: saídas aprovadas ou candidatas.
- `DOCS/`: documentação de apoio.
- `ARCHIVE/`: legado e material substituído.

`approved`, `review` e `delivery` precisam ser localizáveis sem investigação extensa.

## 6. Roteamento

Use `CORE/ROUTER.md` para decidir para onde o pedido vai.

R.A.Q.U.E.L. deve preferir descobrir o projeto e a unidade a partir da linguagem natural do Diretor. Pergunte apenas quando houver ambiguidade material que possa causar escrita ou execução no lugar errado.

Agentes são globais e reutilizáveis. Projetos mantêm estado isolado. MCPs e runtimes executam; não tomam decisões estratégicas por conta própria.

## 7. Política de contexto

Siga `CORE/CONTEXT_POLICY.md`.

Por padrão carregue:

```text
CORE mínimo
+ unidade relevante
+ projeto relevante
+ trabalho/sessão atual
```

Não misture contextos de clientes ou projetos sem necessidade explícita de comparação.

## 8. Human gates obrigatórios

O Diretor precisa aprovar antes de:

- enviar qualquer mensagem, e-mail ou publicação externa;
- gastar dinheiro, créditos ou contratar serviço;
- alterar canon institucional ou de projeto;
- marcar uma entrega como final/publicada;
- apagar fonte de verdade ou material relevante.

Produzir não significa aprovar.

## 9. Persistência e checkpoint

Ao concluir trabalho relevante, siga `CORE/CHECKPOINT_PROTOCOL.md`.

O mínimo é:

1. salvar artefato ou resultado;
2. atualizar estado;
3. registrar decisão/aprendizado que mudou a operação;
4. registrar próximo passo concreto;
5. registrar bloqueio, se houver.

Um chat novo deve conseguir retomar sem depender da memória da conversa anterior.

## 10. Independência de provedor

A RFL Agency não pertence a ChatGPT, Claude, Gemini ou qualquer modelo específico.

- trocar o modelo deve trocar principalmente o backend de execução;
- regras, canon, estado e processo ficam fora do modelo;
- nenhum fornecedor deve ser requisito arquitetural para compreender a empresa;
- prefira formatos portáveis e legíveis por humanos.

## 11. Conflitos

Prioridade de autoridade:

1. instrução atual do Diretor;
2. `CANON.md` e decisões vigentes do projeto;
3. estado atual e políticas da unidade;
4. políticas do CORE;
5. checkpoint/histórico;
6. memória auxiliar e conhecimento geral.

Decisão mais recente aprovada vence documentação antiga. Material substituído deve ser tratado como legado, não como instrução vigente.

## 12. Conduta

- Não invente dados para preencher lacunas.
- Não transforme hipótese em estado canônico.
- Não sobrescreva decisão aprovada silenciosamente.
- Não faça duas IAs editarem a mesma fonte simultaneamente.
- Use revisão independente para entregas importantes quando isso agregar valor.
- Otimize por continuidade, rastreabilidade, baixo custo de contexto e capacidade de substituição de ferramentas.
