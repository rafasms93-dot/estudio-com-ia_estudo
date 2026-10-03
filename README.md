# Estúdio com IA

Uma pasta que ensina qualquer IA a trabalhar no seu estúdio de design, do seu jeito, com os seus clientes.

> Prefere ler antes de instalar? O [guia em PDF](guia-estudio-com-ia.pdf) explica tudo em 9 páginas, sem termo técnico.

---

## A ideia

O que manda não é a IA que você usa. É o sistema em volta dela.

Uma IA solta sabe muita coisa do mundo e nada sobre você. Toda vez você precisa explicar quem é o cliente, como ele fala, o que já foi feito. Aqui é o contrário: tudo que importa fica escrito em arquivos dentro de uma pasta, e qualquer IA que você abrir nessa pasta trabalha lendo esses arquivos. É como colocar a IA numa gaiola onde só existem as informações do seu estúdio e dos seus clientes.

O resultado:

1. **Pedido curto sai certo.** "Faz uma legenda pro cliente X" já basta, porque o tom de voz, o público e as regras dele estão na pasta.
2. **Você não fica preso a uma IA.** Claude, ChatGPT e Gemini leem os mesmos arquivos. Acabou a cota de uma, você abre a mesma pasta na outra e continua de onde parou.
3. **A IA aprende com as suas correções.** Quando você diz "não é assim", a regra vai para o arquivo, e qualquer IA que abrir a pasta depois já sabe.

Só não esquece: você continua sendo o filtro. A IA sugere, você decide.

## As 4 camadas

```
1. Arquitetura de pastas         onde cada coisa mora
2. Configuração das IAs          o manual que toda IA lê ao abrir a pasta
3. Contexto e memória            o que a IA aprende fica salvo e se atualiza sozinho
4. Clientes                      cadastro por entrevista e o cofre de cada cliente
```

### 1. Arquitetura de pastas

```
seu-estudio/
├── README.md          este arquivo
├── INSTALAR.md        o PRD de instalação: a IA lê e executa
├── AGENTS.md          o manual do estúdio (vale para todas as IAs)
├── CLAUDE.md          porta de entrada do Claude → manda para o AGENTS.md
├── GEMINI.md          porta de entrada do Gemini → manda para o AGENTS.md
├── RETOMAR.md         passagem de bastão entre IAs e entre conversas
├── .claude/
│   └── settings.json  hooks do Claude Code (carregam o cofre sozinhos)
├── ferramentas/
│   └── contexto.py    monta o núcleo do cliente para qualquer IA
├── estudio/
│   ├── profile.md     quem é o seu estúdio
│   └── processos.md   como o seu estúdio trabalha, passo a passo
└── clientes/
    ├── _modelo/       modelos de ficha, léxico, estratégia e briefing
    └── nome-do-cliente/
        ├── profile.md     a ficha: quem ele é
        ├── lexico.md      como a marca fala
        ├── estrategia.md  o que vale agora (e o que deixou de valer)
        ├── marca/         logo, manual, fontes, fotos
        └── trabalhos/
            └── 2026-10-03_flyer-sabado/
                ├── briefing.md
                └── (as entregas)
```

As pastas de cliente não vêm prontas: a IA cria cada uma na hora em que o cliente aparece.

### 2. Configuração das IAs

O `AGENTS.md` é o manual único. Ele diz à IA o que ler antes de cada tarefa, como cadastrar cliente, onde salvar cada coisa, o que fazer quando há conflito e o que ela nunca deve fazer sem perguntar.

Cada IA procura um arquivo diferente ao abrir uma pasta: o Claude lê o `CLAUDE.md`, o Gemini lê o `GEMINI.md`, o Codex (ChatGPT) e outros leem o `AGENTS.md` direto. Por isso o `CLAUDE.md` e o `GEMINI.md` só apontam para o `AGENTS.md`. Você escreve a regra uma vez e todas obedecem.

O manual também ensina as IAs a trabalharem juntas na mesma pasta: quem faz o quê, como uma passa o trabalho para a outra (pelo `RETOMAR.md`) e por que quem gerou um trabalho não deve ser quem o revisa.

### 3. Contexto e memória

Ao terminar uma tarefa, a IA salva o que mudou no lugar certo: a entrega vira uma linha no histórico do cliente, a palavra corrigida vai para o léxico, a decisão vai para a estratégia ou para o briefing do trabalho. Ela avisa em uma linha o que salvou, e pergunta antes de mudar algo que já estava escrito.

A memória tem duas camadas:

- **Os arquivos.** São a memória de verdade: você lê, edita e entende tudo que está ali.
- **O MemPalace** (opcional). Um índice de busca que roda no seu computador, de graça, sem mandar nada para a internet. Serve para a IA achar em segundos aquela decisão de três meses atrás sem ler todos os arquivos. Se ele e um arquivo discordarem, vale o arquivo.

### 4. Clientes

Você cita um cliente que a IA não conhece, ela pergunta se pode cadastrar e faz uma entrevista curta (ou lê o material que você mandar: site, Instagram, conversa de WhatsApp, briefing antigo). Com isso ela cria a pasta e o **cofre** dele, três arquivos:

- **`profile.md`**, a ficha: quem o cliente é. Muda devagar.
- **`lexico.md`**, as palavras da marca: o que ela usa, o que ela nunca usa, como se escreve o nome. "Descontraído" a IA interpreta como quiser; "nunca escrever imperdível" não tem como errar.
- **`estrategia.md`**, as decisões: o que vale agora, desde quando e até quando revisar. Quando uma decisão deixa de valer, ela é revogada: fica no arquivo, riscada, para você lembrar, mas a IA nunca mais recebe. Decisão velha ao lado da nova faz a IA misturar as duas. Se uma decisão passa da data de revisão, a IA pergunta se ela continua valendo.

**O cofre entra sozinho na conversa.** No Claude Code, quando o seu pedido cita um cliente, um hook (um gatilho automático do app) coloca o léxico e as decisões em vigor dele na conversa antes de a IA responder. A IA não depende de "lembrar" de ler. O mesmo hook prende a conversa àquele cliente: escrever na pasta de outro é bloqueado, para a voz de uma marca não vazar para a outra. Em outra IA, ela roda o mesmo script (`ferramentas/contexto.py`) por conta própria, porque o manual manda.

**O que é o `profile.md`:** a ficha que a IA lê antes de trabalhar. O do estúdio diz quem você é (serviços, público, como cobra, como fala, o seu olhar). O do cliente diz quem ele é (negócio, público, marca, tom de voz, regras, histórico). Quando você pede algo para um cliente, a IA lê os dois antes de responder. Por isso você não precisa repetir contexto.

**Por que `.md`:** Markdown é texto puro com uma marcação simples (`#` para título, `-` para lista). Toda IA lê, qualquer editor abre (Bloco de Notas, TextEdit, VS Code, Obsidian) e não depende de nenhuma plataforma. Trocou de IA, a ficha vai junto.

**Como ele cresce:** você não preenche tudo de uma vez. Cada correção sua vira uma linha em "Regras aprendidas", cada entrega vira uma linha no "Histórico", o que ficou sem resposta vai sendo perguntado aos poucos. Quanto mais você trabalha, mais a IA acerta de primeira. E você pode abrir e editar à mão quando quiser.

---

## Como instalar

Não precisa saber programar nem abrir o terminal. Quando a IA precisar rodar algum comando, ela explica o que é e pede a sua permissão.

1. Nesta página do GitHub, clique em **Code → Download ZIP**.
2. Descompacte e renomeie a pasta com o nome do seu estúdio. Se ela ficar dentro do Dropbox ou do Google Drive, você ganha backup de graça.
3. Abra a pasta no app de IA que você usa: **Claude** (aba Code do app, ou Claude Code), **Codex** (do ChatGPT) ou **Antigravity** (do Google).
4. Escreva no chat: **"Leia o INSTALAR.md e execute."**

A IA confere a estrutura, faz uma entrevista sobre o seu estúdio (uns 15 minutos), oferece instalar a memória e, se você quiser, já cadastra o seu primeiro cliente.

O cofre usa o Python, que já vem no Mac e no Linux. No Windows, a IA te mostra como instalar se faltar. O Claude Code é onde o cofre carrega sozinho; no Codex e no Antigravity a IA carrega seguindo o manual.

> Sabe usar Git? Pode usar **Use this template** em vez do ZIP. Mas crie o repositório como **privado**: os dados dos seus clientes vão morar nele.

## No dia a dia

É só falar normal. Alguns atalhos:

- **"Cliente novo: [nome]"** → a IA entrevista e cria a pasta.
- **"Trabalho novo pro [cliente]: [o que é]"** → cria a pasta do trabalho com o briefing.
- **"Não é assim, o certo é…"** → vira regra e ela não erra de novo.
- **"O que você sabe do [cliente]?"** → resumo da ficha e do histórico.
- **"Atualiza o contexto"** → ela revisa a conversa e salva o que faltou.
- **"Vou parar por hoje"** → ela anota no `RETOMAR.md` onde parou, e qualquer IA continua dali.

Quer usar outra IA? Abra esta mesma pasta nela. Não precisa configurar nada.

## O que não vem aqui

Esta é a base: estrutura, configuração, contexto, memória e o cofre de clientes. Não vêm skills, fluxos de produção (imagem, vídeo, proposta, apresentação) nem integrações com ferramentas externas. Tudo isso funciona melhor construído em cima desta base, com o seu jeito de trabalhar já registrado.

## Licença

MIT. Use, adapte e distribua à vontade, mantendo o aviso do arquivo [LICENSE](LICENSE).
