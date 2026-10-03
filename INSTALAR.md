# INSTALAR · PRD de instalação

> Você, IA, que está lendo este arquivo: a pessoa pediu para você instalar o sistema do estúdio nesta pasta. Siga as fases na ordem. A pessoa é designer, não programadora.

## Objetivo

No fim da instalação, esta pasta tem:

1. a estrutura conferida e o cofre de cliente funcionando (o autoteste do `ferramentas/contexto.py` passa);
2. a divisão "Quem faz o quê" do `AGENTS.md` ajustada às IAs que a pessoa usa;
3. `estudio/profile.md` e `estudio/processos.md` preenchidos com as respostas da pessoa;
4. a memória MemPalace instalada e conectada, ou a decisão da pessoa de não instalar;
5. se a pessoa quiser, o primeiro cliente cadastrado e, no Claude Code, o carregamento automático dele testado ao vivo.

## Regras de execução

- Fale em português do Brasil, simples e sem jargão técnico. Se precisar de um termo técnico, explique em meia frase.
- Uma fase por vez. No fim de cada fase, diga em uma ou duas linhas o que foi feito.
- Antes de rodar qualquer comando no computador, diga em uma frase o que ele faz.
- Não apague nem sobrescreva o que a pessoa já tiver na pasta. Na dúvida, mostre e pergunte.
- Nunca invente informação do estúdio (preço, prazo, política). O que a pessoa não respondeu vira pendência.
- Se a conversa cair no meio, o progresso está nos arquivos. Na próxima, continue de onde parou: os comentários `<!-- Pergunte` que sobraram em `estudio/profile.md` e `estudio/processos.md` são os blocos que ainda faltam.

## Fase 1 · Conferir a estrutura

1. Confira se existem: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `RETOMAR.md`, `estudio/profile.md`, `estudio/processos.md`, os quatro modelos em `clientes/_modelo/` (`profile.md`, `lexico.md`, `estrategia.md`, `briefing.md`), `ferramentas/contexto.py` e `.claude/settings.json`. Se faltar algum, diga qual e peça para a pessoa baixar o pacote de novo. Não recrie de cabeça. (A pasta `.claude` fica oculta no Finder e no Explorer; é normal.)
2. **Python.** Confira se existe Python 3.8 ou mais novo (`python3 --version`). O cofre de cliente e a memória precisam dele. Se não existir, explique como instalar pelo [python.org](https://www.python.org/downloads/) e siga com a instalação: até o Python chegar, o Claude Code mostra um aviso de hook com erro a cada mensagem, e qualquer IA lê o cofre direto dos arquivos (seção 3 do `AGENTS.md`).
3. **Autoteste do cofre.** Rode `python3 ferramentas/contexto.py --teste`. Tem que terminar com "autoteste do contexto.py ok". Se falhar, mostre o erro para a pessoa e não siga para a Fase 4.
4. Explique em quatro linhas: `AGENTS.md` é o manual que toda IA lê ao abrir a pasta; `estudio/` é o estúdio dela; `clientes/` vai ganhar uma pasta por cliente, criada na hora em que ele aparecer; e cada cliente tem um cofre (ficha, léxico e estratégia) que entra na conversa antes de qualquer peça. Se o app for Claude Code, avise que ele pode pedir para confiar na pasta ou aprovar os hooks dela: é para aceitar, é isso que carrega o cofre sozinho.
5. Pergunte quais IAs ela usa ou assina (Claude, ChatGPT, Gemini, outra). Ajuste a tabela "Quem faz o quê" da seção 7 do `AGENTS.md`: tire as linhas das IAs que ela não usa e acrescente as que faltarem. Se ela usa só uma, deixe só essa linha com "faz tudo".

## Fase 2 · Entrevista do estúdio

O objetivo é preencher `estudio/profile.md` e `estudio/processos.md`. As perguntas estão nos próprios arquivos, nos comentários `<!-- Pergunte: ... -->`.

1. Diga em duas linhas o que vai acontecer: umas perguntas em blocos, uns 15 minutos, dá para pular qualquer uma.
2. **Peça material pronto primeiro:** bio do Instagram, texto do site ou do portfólio, uma proposta ou um orçamento antigo, uma apresentação. Leia o que vier, preencha o que der e diga o que já ficou preenchido.
3. Siga os blocos na ordem: primeiro os de `estudio/profile.md`, depois os de `estudio/processos.md`. **Um bloco por mensagem**, com as perguntas numeradas para a pessoa responder por número. Pule o que o material já respondeu.
4. A cada resposta, grave o bloco no arquivo na mesma hora:
   - escreva em texto limpo e direto, não como transcrição;
   - na seção "Nossa voz", mantenha as palavras da própria pessoa;
   - troque o título `# Nome do estúdio` pelo nome real;
   - apague o comentário `<!-- Pergunte` daquele bloco;
   - o que ficou sem resposta vai para `## Pendências`, como pergunta.
5. Se a pessoa disser que não tem um processo definido, sugira este e deixe ela ajustar: primeiro contato → orçamento → proposta → aprovação e sinal → briefing → criação → apresentação → ajustes → entrega dos arquivos → pós-venda.
6. No fim, mostre um resumo do estúdio em até 5 linhas e pergunte: "Isso é você? Quer mudar alguma coisa?". Ajuste e preencha a data em `atualizado:` nos dois arquivos.

## Fase 3 · Memória com MemPalace (opcional)

Explique em duas linhas o que é (índice de busca no próprio computador, gratuito, nada sai da máquina) e pergunte se a pessoa quer instalar agora. Avise que precisa de uns 300 MB livres e de internet só na instalação. Se ela não quiser, ou se algo der errado, pule para a Fase 4: o sistema funciona sem isso.

**Fontes oficiais, e só elas:** [github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace), [pypi.org/project/mempalace](https://pypi.org/project/mempalace/) e [mempalaceofficial.com](https://mempalaceofficial.com). Existem sites falsos com nome parecido (por exemplo `mempalace.tech`) que distribuem malware. Não instale nada de outro endereço.

1. **Python.** O MemPalace precisa do Python 3.9 ou mais novo (conferido na Fase 1). Se a versão for mais velha ou não houver Python, encerre a fase.
2. **Instalar.** Use `uv tool install mempalace`. Se não houver `uv`, use `pipx install mempalace`. Se não houver nenhum dos dois, pergunte se pode instalar o `uv` pela documentação oficial em [docs.astral.sh/uv](https://docs.astral.sh/uv/).
3. **Iniciar na pasta.** Rode `mempalace init . --yes` dentro desta pasta. Ele cria a configuração da memória (o arquivo `mempalace.yaml` aqui e a pasta `~/.mempalace/`). Avise a pessoa que esse arquivo é da memória e não precisa ser mexido.
4. **Português.** Antes de indexar qualquer coisa, abra `~/.mempalace/config.json` e acrescente `"embedding_model": "embeddinggemma"`, sem apagar o que já existe. O modelo padrão foi treinado só em inglês e busca mal em português; o `embeddinggemma` é multilíngue. Trocar depois de indexar obriga a reconstruir o índice (`mempalace repair rebuild-index`). Na primeira indexação ele baixa o modelo (uns 300 MB).
5. **Indexar e testar.** Rode `mempalace mine .` e depois `mempalace search` com o nome do estúdio. Tem que aparecer o `estudio/profile.md`.
6. **Conectar ao app.** Rode `mempalace mcp`: ele mostra o comando exato de conexão para este computador. Aplique para o app em uso (Claude Code e Codex têm comando próprio; no Antigravity, siga o guia oficial em mempalaceofficial.com/guide/antigravity). Peça para a pessoa reiniciar o app e confirme que a ferramenta `mempalace_status` responde.
   - Erro comum: o comando de conexão aponta para um Python que não tem o MemPalace (acontece com `uv` e `pipx`). Use o comando que o `mempalace mcp` imprimiu, ou o executável `mempalace-mcp`, em vez de um `python -m` genérico.
7. **Opcional:** se o app for Claude Code ou Codex, ofereça ligar o salvamento automático das conversas na memória (guia oficial em mempalaceofficial.com/guide/hooks). O Claude Code apaga conversas antigas depois de um tempo; isso guarda uma cópia antes.

## Fase 4 · Primeiro cliente e entrega

1. Pergunte se a pessoa quer cadastrar o primeiro cliente agora. Se sim, siga "Cliente novo" na seção 4 do `AGENTS.md` (ficha, léxico e estratégia). Depois rode `python3 ferramentas/contexto.py [slug]` e mostre o núcleo que saiu: é isso que toda IA vai receber antes de produzir para esse cliente.
2. **Teste ao vivo, se o app for Claude Code:** peça para a pessoa mandar "faz uma legenda de teste pro [nome do cliente]". Na sua próxima resposta, confirme que a conversa recebeu o bloco `[Contexto do cliente · carregado automaticamente]`. Se não recebeu, os hooks não foram aprovados: peça para a pessoa reabrir a pasta e aceitar.
3. Rode a lista de aceite abaixo e mostre o resultado (✅ ou ❌ com o motivo).
4. Termine com esta mensagem, adaptada ao que foi instalado:

> Pronto. No dia a dia, é só falar normal. Alguns atalhos:
> - **"Cliente novo: [nome]"** → eu te entrevisto e crio a pasta dele.
> - **"Trabalho novo pro [cliente]: [o que é]"** → crio a pasta do trabalho com o briefing.
> - **"Não é assim, o certo é…"** → anoto no lugar certo (palavra no léxico, decisão na estratégia) e não erro de novo.
> - **"A partir de agora, [decisão]"** → vira decisão vigente do cliente, com data de revisão. A antiga é revogada.
> - **"O que você sabe do [cliente]?"** → resumo da ficha e do histórico.
> - **"Atualiza o contexto"** → reviso a conversa e salvo o que faltou.
> - **"Vou parar por hoje"** → anoto no RETOMAR.md onde paramos.
>
> Quer usar outra IA? Abra esta mesma pasta nela. Não precisa configurar nada.

## Lista de aceite

- [ ] Os arquivos da Fase 1 existem; `CLAUDE.md` e `GEMINI.md` apontam para o `AGENTS.md`.
- [ ] `python3 ferramentas/contexto.py --teste` passa, **ou** a pessoa sabe que precisa instalar o Python.
- [ ] A tabela "Quem faz o quê" do `AGENTS.md` lista só as IAs que a pessoa usa.
- [ ] `estudio/profile.md` e `estudio/processos.md` sem nenhum `<!-- Pergunte` (o que não foi respondido está em `## Pendências`).
- [ ] `estudio/processos.md` tem o atendimento em passos numerados.
- [ ] Os quatro modelos de `clientes/_modelo/` intactos, com os comentários de pergunta.
- [ ] Se houve primeiro cliente: o núcleo dele sai no `contexto.py` e, no Claude Code, entrou sozinho no teste ao vivo.
- [ ] MemPalace: `mempalace_status` responde no app, **ou** a pessoa escolheu não instalar.
- [ ] A pessoa recebeu a mensagem final com os atalhos.

Este arquivo pode ficar na pasta: ele serve para retomar ou refazer a instalação.
