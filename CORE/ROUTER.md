# RFL Agency · Router

O Router transforma um pedido curto do Diretor em uma rota operacional.

## Objetivo

Evitar que Rafael precise:

- descobrir manualmente qual MARK abrir;
- procurar pastas e arquivos de contexto;
- iniciar um chat especializado para cada frente;
- escolher modelo, agente ou ferramenta antes de formular a tarefa.

## Classificação mínima

Para cada entrada, inferir quando possível:

```yaml
natureza: cliente | interno | produto | p&d | administrativo | estudo
unidade: identificador da unidade responsável
projeto: projeto MARK ou produto relacionado
trabalho: demanda/sessão específica, se houver
estado: ideia | planejado | em-andamento | aguardando | bloqueado | revisão | concluído
impacto: receita | custo | operação | aprendizado | infraestrutura | propriedade-intelectual
risco: baixo | gate-humano | ambíguo
```

Não é necessário expor essa ficha ao Diretor em toda interação. Ela serve ao roteamento.

## Fluxo

1. **Entender a intenção.** O que precisa acontecer?
2. **Resolver entidades.** Cliente, projeto, unidade, trabalho e prazo citados.
3. **Localizar fonte de verdade.** Notion, Drive/Sheets, GitHub, workstation ou outra fonte canônica registrada.
4. **Carregar contexto mínimo.** Aplicar `CONTEXT_POLICY.md`.
5. **Selecionar capacidade.** Agente, playbook, pipeline, ferramenta e backend.
6. **Executar.** Trabalhar dentro do escopo resolvido.
7. **Validar.** Aplicar gates técnicos e humanos.
8. **Persistir.** Aplicar `CHECKPOINT_PROTOCOL.md`.

## Ordem para resolver destino

1. Entidades explícitas no pedido atual.
2. Sessão/projeto ativo já identificado.
3. Estado operacional no MARK/Notion.
4. Índice de projetos e unidades.
5. Busca semântica ou textual nas fontes autorizadas.
6. Pergunta ao Diretor somente quando permanecer ambiguidade material.

## Regra de ambiguidade

Não adivinhar quando um erro de roteamento puder:

- alterar o projeto errado;
- misturar identidade de clientes;
- gerar gasto;
- enviar/publicar conteúdo;
- mudar canon;
- destruir ou sobrescrever informação relevante.

Para ambiguidades de baixo impacto, prefira resolver pela evidência disponível e continuar.

## Troca de backend

O Router decide por **capacidade necessária**, não por marca de IA.

Exemplos de capacidades:

- raciocínio e planejamento;
- pesquisa externa;
- programação;
- visão/análise de mídia;
- geração de imagem;
- edição de imagem/vídeo;
- operação de documentos/planilhas;
- revisão/QC.

O backend concreto pode mudar sem alterar o contrato do projeto.

## Exemplos

### "Nova demanda da Drumtech"

```text
natureza: cliente
unidade: M8
projeto/cliente: Drumtech
→ carregar regras M8 + contexto Drumtech + trabalho atual
```

### "Vamos continuar a cena do limão do Nico & Theo"

```text
natureza: p&d/produção
unidade: M11
projeto: Nico & Theo
trabalho: cena do limão
→ carregar canon + estado + checkpoint + pipeline necessário
```

### "Paguei a conta X"

```text
natureza: administrativo
unidade: M0
→ registrar diretamente na fonte financeira de verdade
```

## Resultado esperado

Para o Diretor, a interface deve parecer simples:

> dizer a tarefa → receber o trabalho no contexto correto.

A complexidade de localização e coordenação pertence ao sistema.
