# RFL Agency · Política de contexto

## Objetivo

Carregar informação suficiente para executar corretamente sem despejar toda a empresa dentro de cada conversa.

## Pacote mínimo padrão

```text
CORE mínimo
+ unidade responsável
+ projeto/cliente relevante
+ trabalho ou sessão atual
```

## O que pertence ao CORE mínimo

- identidade e cadeia de autoridade da Agency;
- regras globais de governança;
- roteamento;
- human gates;
- protocolo de persistência.

Não incluir histórico extenso quando ele não for necessário.

## Contexto de unidade

Carregar apenas regras, processos e capacidades daquela unidade.

Exemplos:

- M8: produção criativa/comercial, clientes, precificação e processo visual.
- M11: produção cinematográfica assistida por IA, System Core, pipelines e gates técnicos.
- M0: operação administrativa e financeira.

## Contexto de projeto

Quando houver projeto MARK, priorizar:

1. `PROJECT.md`
2. `CANON.md`
3. `STATE.md`
4. `CHECKPOINT.md`
5. arquivos adicionais somente quando exigidos pela tarefa.

O histórico bruto não substitui o estado atual.

## Contexto de cliente

Não misturar clientes por conveniência.

Ao trabalhar para um cliente, carregar apenas fatos, regras, decisões e materiais pertinentes a ele e ao trabalho atual. Comparações entre clientes são permitidas quando forem a própria tarefa.

## Fontes externas ao repositório

O Router deve buscar contexto na fonte correta em vez de duplicá-lo aqui:

- Notion para operação, decisões, sessões, conhecimento e status;
- Drive/Sheets para dados, arquivos e planilhas;
- GitHub para código, contratos e versões;
- workstation para produção local;
- Miro somente como mapa visual.

## Economia de contexto

Antes de carregar um arquivo, pergunte internamente:

> este conteúdo pode alterar a decisão ou a execução desta tarefa?

Se não, não carregue.

## Continuidade

Para retomar trabalho, prefira `CHECKPOINT.md` + `STATE.md` a reler toda a conversa anterior.

O objetivo é que conversas sejam descartáveis e o estado institucional seja persistente.
