# RFL Agency · Protocolo de checkpoint

Checkpoint é o ponto seguro de retomada de uma tarefa, sessão ou projeto.

## Quando registrar

Registrar quando:

- uma sessão de trabalho for encerrada;
- houver mudança relevante de estado;
- uma decisão for aprovada;
- uma entrega atingir gate importante;
- o trabalho ficar aguardando cliente, recurso ou validação;
- houver troca de IA, backend ou conversa;
- existir risco de perder contexto operacional.

## Conteúdo mínimo

```markdown
# CHECKPOINT

- Data/hora:
- Unidade:
- Projeto:
- Trabalho/sessão:
- Estado: em-andamento | aguardando | bloqueado | revisão | concluído

## Feito
- resultado concreto já produzido

## Decidido
- decisões aprovadas que governam a próxima etapa

## Próxima ação
- uma ação concreta e executável

## Bloqueios
- nenhum | descrição objetiva

## Fontes/artefatos
- links, caminhos ou IDs necessários para retomar

## Não fazer
- caminhos já rejeitados, quando relevantes
```

## Regra de qualidade

Um checkpoint é suficiente quando outra IA consegue continuar sem perguntar "onde paramos?".

Não transformar checkpoint em diário completo. Ele representa o **estado útil para continuação**.

## Persistência

Além do checkpoint:

1. artefatos devem estar na fonte correta;
2. `STATE.md` deve refletir o estado vigente;
3. decisões canônicas aprovadas devem ir para `CANON.md` ou fonte institucional equivalente;
4. aprendizados processuais recorrentes devem ser promovidos ao processo/knowledge apropriado.

## Sessões

Sessões são registros operacionais vinculados ao projeto, não a própria fonte de verdade do projeto.

Ao encerrar uma sessão:

```text
entrega/resultado
→ estado atualizado
→ decisão/aprendizado persistido
→ próxima ação
→ checkpoint
```

A conversa pode então ser descartada sem perda institucional.
