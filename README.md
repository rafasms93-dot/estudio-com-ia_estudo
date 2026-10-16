# RFL Agency

**RFL Agency** é a camada organizacional de uma empresa AI-native de uma pessoa.

Rafael dirige. A R.A.Q.U.E.L. interpreta e roteia. O MARK mantém estado, regras, projetos e continuidade. Agentes, modelos e ferramentas executam partes do trabalho conforme o contexto mínimo necessário.

## Princípio central

A pessoa não deve precisar procurar pasta, reconstruir contexto ou escolher manualmente qual IA usar para cada tarefa.

O fluxo canônico é:

```text
ENTRADA
  ↓
CLASSIFICAR
  ↓
ROTEAR
  ↓
CARREGAR CONTEXTO MÍNIMO
  ↓
EXECUTAR
  ↓
VALIDAR
  ↓
PERSISTIR
```

## Papéis

- **Rafael — Diretor:** define direção, prioridades e decisão final.
- **R.A.Q.U.E.L. — Orquestradora:** entende o pedido, identifica projeto/unidade, reúne contexto, seleciona capacidade e coordena a execução.
- **MARK — Sistema Operacional:** mantém a verdade institucional sobre projetos, estado, regras, decisões, prioridades, histórico e checkpoints.
- **Agentes / IAs / ferramentas:** executam funções especializadas. São substituíveis; o sistema não depende de um provedor específico.

## Fontes de verdade

- **Notion:** operação, conhecimento, decisões, processos, status e gestão.
- **Google Drive / Sheets:** arquivos, dados estruturados, planilhas e materiais compartilhados.
- **GitHub:** código, contratos operacionais, automações, runtimes e versionamento técnico.
- **Workstation:** produção local e arquivos de trabalho pesados.
- **Miro:** mapa visual e arquitetura; nunca substitui a fonte de verdade.

## Estrutura desta versão

```text
RFL Agency/
├── AGENTS.md
├── README.md
├── CORE/
│   ├── AGENCY.md
│   ├── ROUTER.md
│   ├── CONTEXT_POLICY.md
│   ├── CHECKPOINT_PROTOCOL.md
│   └── UNITS.md
├── clientes/                 legado do sistema-base estudado
├── estudio/                  legado do sistema-base estudado
└── ferramentas/              protótipos e referência técnica
```

Os diretórios herdados do repositório original permanecem nesta fase como referência de P&D. Eles não são, por si só, a arquitetura canônica da RFL Agency.

## Estado

**v0.1 — Fundação de governança.**

Objetivo desta fase: fazer qualquer IA que entre neste repositório entender a empresa, a cadeia de autoridade, o roteamento e o protocolo de continuidade antes de começarmos a automatizar descoberta de contexto e execução.
