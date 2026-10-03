#!/usr/bin/env python3
"""contexto.py · o núcleo do cliente, montado do mesmo jeito para qualquer IA.

O núcleo é o que a IA não tem como adivinhar sozinha: como a marca fala
(lexico.md) e as decisões em vigor (estrategia.md, só a seção "Vigente").
Decisão revogada fica no arquivo para a pessoa, mas nunca entra no contexto:
com a velha ao lado da nova, a IA mistura as duas. Decisão que passou da data
de revisão entra marcada como vencida.

Uso, em qualquer IA:
    python3 ferramentas/contexto.py <slug>      mostra o núcleo do cliente
    python3 ferramentas/contexto.py --teste     autoteste

Hooks do Claude Code (ligados em .claude/settings.json; não precisa rodar à mão):
    --hook pedido      o pedido cita um cliente: o núcleo entra no contexto e a conversa fica com ele
    --hook trava       bloqueia escrita na pasta de outro cliente
    --hook compactou   reinjeta o núcleo depois que a conversa é compactada

Só biblioteca padrão. Python 3.8 ou mais novo.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import shlex
import sys
import tempfile
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CLIENTES = RAIZ / "clientes"

# Pedido de produção. Sem uma destas palavras, citar o cliente não carrega o núcleo:
# "como foi a reunião com o X?" não precisa do léxico dele. Tudo sem acento.
INTENCAO = {
    "legenda", "legendas", "copy", "texto", "textos", "post", "posts", "stories", "story",
    "reel", "reels", "roteiro", "roteiros", "carrossel", "anuncio", "anuncios", "criativo",
    "criativos", "campanha", "pauta", "briefing", "proposta", "apresentacao", "flyer",
    "arte", "artes", "peca", "pecas", "logo", "banner", "cartaz", "convite", "cardapio",
    "email", "mensagem", "resposta", "conteudo", "prompt", "imagem", "imagens",
    "cria", "criar", "escreve", "escrever", "faz", "fazer", "monta", "montar", "gera", "gerar",
    "produz", "produzir", "revisa", "revisar", "ajusta", "ajustar", "refaz", "refazer",
}
# Pedaço de nome que sozinho não identifica cliente nenhum.
GENERICAS = {
    "bar", "cafe", "casa", "loja", "studio", "estudio", "clinica", "restaurante", "academia",
    "grupo", "store", "shop", "oficial", "das", "dos", "del", "the", "and", "com", "pro", "pra",
}


# ─── leitura dos arquivos ────────────────────────────────────────────────────

def tokens(texto: str) -> set:
    """Palavras minúsculas e sem acento: "Estúdio" e "estudio" são a mesma coisa."""
    sem = "".join(c for c in unicodedata.normalize("NFD", texto or "")
                  if unicodedata.category(c) != "Mn")
    return set(re.findall(r"[a-z0-9]+", sem.lower()))


def frontmatter(arquivo: Path) -> dict:
    """Pares `chave: valor` do cabeçalho YAML. Simples de propósito: sem dependência."""
    try:
        texto = arquivo.read_text(encoding="utf-8")
    except OSError:
        return {}
    if not texto.startswith("---"):
        return {}
    campos = {}
    for linha in texto.split("\n---", 1)[0].splitlines()[1:]:
        chave, sep, valor = linha.partition(":")
        if sep and not linha.startswith((" ", "#")):
            campos[chave.strip()] = valor.split(" #")[0].strip().strip("\"'")
    return campos


def secao(arquivo: Path, titulo: str) -> str:
    """Corpo de `## titulo`, sem comentários e sem linha de modelo vazia."""
    try:
        texto = arquivo.read_text(encoding="utf-8")
    except OSError:
        return ""
    m = re.search(rf"^##\s+{re.escape(titulo)}\s*$(.*?)(?=^##\s|\Z)", texto, re.M | re.S)
    if not m:
        return ""
    corpo = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S)
    linhas = [l for l in corpo.splitlines()
              if l.strip() and l.strip() != "-" and not re.fullmatch(r"[|\s:-]*", l.strip())]
    if len(linhas) == 1 and linhas[0].lstrip().startswith("|"):
        return ""  # tabela só com o cabeçalho
    return "\n".join(linhas)


def vigentes(arquivo: Path, hoje: dt.date) -> str:
    """Seção "Vigente", com aviso nas decisões que passaram da data de revisão."""
    saida = []
    for linha in secao(arquivo, "Vigente").splitlines():
        saida.append(linha)
        m = re.search(r"Revisar em:\W*(\d{4}-\d{2}-\d{2})", linha)
        if m and m.group(1) < hoje.isoformat():
            saida.append(f"  ⚠️ VENCIDA desde {m.group(1)}: pergunte se renova ou revoga antes de usar.")
    return "\n".join(saida)


def cadastrados():
    """[(slug, nome)] de cada pasta de cliente. `_modelo` e afins ficam de fora."""
    if not CLIENTES.is_dir():
        return []
    return [(d.name, frontmatter(d / "profile.md").get("nome", ""))
            for d in sorted(CLIENTES.iterdir())
            if d.is_dir() and not d.name.startswith(("_", "."))]


def montar(slug: str, hoje: dt.date | None = None) -> str:
    hoje = hoje or dt.date.today()
    pasta = CLIENTES / slug
    if slug.startswith(("_", ".")) or not pasta.is_dir():
        existentes = ", ".join(s for s, _ in cadastrados()) or "nenhum"
        return f"ERRO: o cliente `{slug}` não existe em clientes/. Cadastrados: {existentes}."

    fm = frontmatter(pasta / "profile.md")
    cabecalho = f"CLIENTE: {fm.get('nome') or slug} ({slug})"
    if fm.get("status"):
        cabecalho += f" · {fm['status']}"
    saida = [cabecalho]
    servico = fm.get("servico", "").strip("[] ")
    if servico:
        saida.append(f"SERVIÇO: {servico}")
    saida.append(f"Ficha completa em clientes/{slug}/profile.md: leia antes de produzir.")

    lexico = pasta / "lexico.md"
    blocos = [(t, secao(lexico, t)) for t in ("Usa", "Nunca", "Grafia fixa", "Exceções")]
    blocos = [(t, b) for t, b in blocos if b]
    if blocos:
        saida.append("\nLÉXICO · como esta marca fala:")
        saida += [f"[{t}]\n{b}" for t, b in blocos]
    else:
        saida.append("\nLÉXICO: vazio ainda.")

    vig = vigentes(pasta / "estrategia.md", hoje)
    saida.append("\nDECISÕES VIGENTES · governam o que se produz agora:\n" + vig if vig
                 else "\nDECISÕES VIGENTES: nenhuma.")

    pend = secao(pasta / "profile.md", "Pendências")
    if pend:
        saida.append("\nPENDÊNCIAS DO CADASTRO (não trate como fato):\n" + pend[:400])
    return "\n".join(saida)


def citado(texto: str):
    """(slug, empatados). Um cliente só, ou a lista quando dá empate.

    Empate vira pergunta, nunca escolha: o núcleo do cliente errado é pior que
    nenhum, porque a peça sai plausível na voz de outra marca.
    """
    palavras = tokens(texto)
    achados = []
    for slug, nome in cadastrados():
        chaves = {k for k in tokens(slug) | tokens(nome) if len(k) > 2 and k not in GENERICAS}
        if chaves & palavras:
            achados.append((len(chaves & palavras), slug))
    if not achados:
        return None, []
    achados.sort(reverse=True)
    topo = [s for n, s in achados if n == achados[0][0]]
    return (topo[0], []) if len(topo) == 1 else (None, sorted(topo))


# ─── conversa presa a um cliente ─────────────────────────────────────────────

def _arquivo_pin(payload: dict):
    sid = re.sub(r"[^\w-]", "", str(payload.get("session_id") or ""))[:40]
    return Path(tempfile.gettempdir()) / f"estudio-cliente-{sid}" if sid else None


def ler_pin(payload: dict):
    arq = _arquivo_pin(payload)
    if not arq:
        return None
    try:
        return arq.read_text(encoding="utf-8").strip() or None
    except OSError:
        return None


def fixar(payload: dict, slug: str):
    arq = _arquivo_pin(payload)
    if arq:
        try:
            arq.write_text(slug, encoding="utf-8")
        except OSError:
            pass


# ponytail: lê o comando de shell por padrão de texto; não enxerga escrita feita
# de dentro de um script (python -c, node -e). Teto real seria isolar a escrita por pasta.
_REDIR = re.compile(r"(?:>>?|\btee\b(?:\s+-a)?)\s*(?:\"([^\"]+)\"|'([^']+)'|([^\s|;&<>]+))")
_TODOS = re.compile(r"\b(?:mkdir|touch)\b([^;&|]*)")
_COPIA = re.compile(r"\b(?:cp|mv|rsync)\b([^;&|]*)")
_SED_I = re.compile(r"\bsed\s+-i\S*\s+(?:'[^']*'|\"[^\"]*\"|\S+)\s+([^;&|]+)")


def _args(trecho: str):
    try:
        return [a for a in shlex.split(trecho) if not a.startswith("-")]
    except ValueError:
        return [a.strip("\"'") for a in trecho.split() if not a.startswith("-")]


def destinos(comando: str):
    """Caminhos em que um comando de shell ESCREVE (não os que ele só lê)."""
    alvos = [next(g for g in m.groups() if g) for m in _REDIR.finditer(comando)]
    for m in _TODOS.finditer(comando):
        alvos += _args(m.group(1))
    for m in _COPIA.finditer(comando):
        args = _args(m.group(1))
        if args:
            alvos.append(args[-1])
    for m in _SED_I.finditer(comando):
        alvos += _args(m.group(1))
    return alvos


def cliente_do_caminho(caminho: str, cwd):
    """Slug do cliente dono do caminho, ou None se for fora de clientes/."""
    if not caminho:
        return None
    alvo = os.path.realpath(os.path.join(cwd or str(RAIZ), os.path.expanduser(caminho)))
    try:
        rel = os.path.relpath(alvo, os.path.realpath(CLIENTES))
    except ValueError:  # outro disco, no Windows
        return None
    if rel == "." or rel.startswith(".."):
        return None
    return rel.split(os.sep)[0]


def avaliar_trava(payload: dict, pin):
    """(bloqueia, mensagem, pin). Sem efeito colateral, para dar para testar."""
    entrada = payload.get("tool_input") or {}
    ferramenta = payload.get("tool_name")
    if ferramenta in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        caminhos = [entrada.get("file_path") or entrada.get("notebook_path") or ""]
    elif ferramenta == "Bash":
        caminhos = destinos(entrada.get("command") or "")
    else:
        return False, "", pin  # ler outro cliente é livre: comparar é trabalho legítimo
    for caminho in caminhos:
        alvo = cliente_do_caminho(caminho, payload.get("cwd"))
        if not alvo or alvo.startswith(("_", ".")) or alvo == pin:
            continue
        if not (CLIENTES / alvo).exists():
            pin = alvo  # cliente sendo cadastrado agora: a conversa passa a ser dele
            continue
        if pin:
            return True, (
                f"BLOQUEADO: esta conversa está trabalhando no cliente `{pin}` e você tentou "
                f"escrever em `clientes/{alvo}/`. Um cliente por conversa evita que a voz de "
                f"uma marca vaze para outra. Diga à pessoa: para trocar, é só citar o cliente "
                f"{alvo} no próximo pedido, ou abrir uma conversa nova."), pin
    return False, "", pin


# ─── hooks ───────────────────────────────────────────────────────────────────

def hook_pedido(payload: dict) -> int:
    texto = payload.get("prompt") or ""
    if "<task-notification>" in texto:
        return 0  # aviso de tarefa em segundo plano não é pedido da pessoa
    slug, empate = citado(texto)
    if slug:
        fixar(payload, slug)  # o último cliente citado é o cliente da conversa
    if not tokens(texto) & INTENCAO:
        return 0
    if empate:
        print(f"[Contexto do cliente] O pedido pode ser de mais de um cliente "
              f"({', '.join(empate)}). Pergunte qual antes de produzir.")
    elif slug:
        # ponytail: injeta a cada pedido que cita o cliente; se pesar, injetar só quando o cliente muda
        print("[Contexto do cliente · carregado automaticamente]\n" + montar(slug))
    return 0


def hook_trava(payload: dict) -> int:
    pin = ler_pin(payload)
    bloqueia, mensagem, novo = avaliar_trava(payload, pin)
    if novo and novo != pin:
        fixar(payload, novo)
    if bloqueia:
        print(mensagem, file=sys.stderr)
        return 2
    return 0


def hook_compactou(payload: dict) -> int:
    pin = ler_pin(payload)
    if pin and (CLIENTES / pin).is_dir():
        print("[Contexto do cliente · reinjetado depois da compactação]\n" + montar(pin))
    return 0


HOOKS = {"pedido": hook_pedido, "trava": hook_trava, "compactou": hook_compactou}


def main(argv) -> int:
    if "--teste" in argv:
        return teste()
    if "--hook" in argv:
        nome = argv[argv.index("--hook") + 1] if len(argv) > argv.index("--hook") + 1 else ""
        try:
            return HOOKS[nome](json.load(sys.stdin))
        except Exception:
            return 0  # hook com defeito nunca trava a conversa
    slugs = [a for a in argv if not a.startswith("--")]
    if not slugs:
        print(__doc__)
        return 2
    texto = montar(slugs[0])
    print(texto)
    return 1 if texto.startswith("ERRO") else 0


# ─── autoteste ───────────────────────────────────────────────────────────────

def teste() -> int:
    global RAIZ, CLIENTES
    original = (RAIZ, CLIENTES)
    modelo = original[1] / "_modelo"
    with tempfile.TemporaryDirectory() as tmp:
        RAIZ = Path(tmp)
        CLIENTES = RAIZ / "clientes"
        pad, motos = CLIENTES / "padaria-sao-jorge", CLIENTES / "sao-jorge-motos"
        for pasta in (pad, motos):
            pasta.mkdir(parents=True)
            for nome in ("profile.md", "lexico.md", "estrategia.md"):
                (pasta / nome).write_text((modelo / nome).read_text(encoding="utf-8"), encoding="utf-8")

        # cliente recém-copiado do modelo: nada do molde vaza para o contexto
        vazio = montar("sao-jorge-motos")
        assert "Pergunte" not in vazio and "AAAA" not in vazio and "Em vez de" not in vazio, vazio
        assert "LÉXICO: vazio" in vazio and "DECISÕES VIGENTES: nenhuma" in vazio, vazio

        (pad / "profile.md").write_text(
            '---\ntipo: cliente\nnome: "Padaria São Jorge"\nslug: padaria-sao-jorge\n'
            'status: ativo   # comentário\nservico: [social-media, flyer]\n---\n\n'
            '## Pendências\n- horário de domingo\n', encoding="utf-8")
        (pad / "lexico.md").write_text(
            "## Usa\n\n| Em vez de | Escreva | Por quê |\n|---|---|---|\n"
            "| clientes | vizinhos | pedido dele |\n\n## Nunca\n\n- imperdível\n\n"
            "## Grafia fixa\n\n- Padaria São Jorge, sempre com acento\n", encoding="utf-8")
        (pad / "estrategia.md").write_text(
            "## Vigente\n\n### Foco no café da manhã\n"
            "- **Desde:** 2026-09-01 · **Revisar em:** 2026-09-30\n- **Decisão:** só café da manhã\n\n"
            "### Sem preço no feed\n- **Desde:** 2026-08-01 · **Revisar em:** —\n\n"
            "## Revogadas\n\n- ~~postar todo dia~~ · revogada em 2026-08-01\n", encoding="utf-8")

        pac = montar("padaria-sao-jorge", hoje=dt.date(2026, 10, 3))
        assert "CLIENTE: Padaria São Jorge (padaria-sao-jorge) · ativo" in pac, pac
        assert "SERVIÇO: social-media, flyer" in pac, pac
        assert "vizinhos" in pac and "imperdível" in pac and "sempre com acento" in pac, pac
        assert "café da manhã" in pac and "Sem preço no feed" in pac, pac
        assert "postar todo dia" not in pac, "decisão revogada vazou para o contexto"
        assert pac.count("VENCIDA") == 1 and "VENCIDA desde 2026-09-30" in pac, pac
        assert "horário de domingo" in pac, pac
        assert montar("nao-existe").startswith("ERRO") and montar("_modelo").startswith("ERRO")

        # quem é citado
        assert citado("faz uma legenda pra Padaria São Jorge") == ("padaria-sao-jorge", [])
        assert citado("legenda pra padaria sao jorge")[0] == "padaria-sao-jorge"  # sem acento
        assert citado("legenda pro São Jorge") == (None, ["padaria-sao-jorge", "sao-jorge-motos"])
        assert citado("legenda pro bar") == (None, [])  # palavra genérica não aponta ninguém
        assert not tokens("como foi a reunião com a padaria?") & INTENCAO

        # trava
        sid = {"session_id": "teste-contexto-py", "cwd": str(RAIZ)}
        w = lambda p: dict(sid, tool_name="Write", tool_input={"file_path": str(p)})
        sh = lambda c: dict(sid, tool_name="Bash", tool_input={"command": c})
        pin = "padaria-sao-jorge"
        assert not avaliar_trava(w(pad / "x.md"), None)[0]  # sem cliente na conversa, livre
        assert not avaliar_trava(w(pad / "trabalhos" / "x.md"), pin)[0]
        assert avaliar_trava(w(motos / "x.md"), pin)[0]  # outro cliente: bloqueia
        assert not avaliar_trava(w(CLIENTES / "_modelo" / "x.md"), pin)[0]
        assert not avaliar_trava(w(RAIZ / "estudio" / "profile.md"), pin)[0]
        assert not avaliar_trava(dict(sid, tool_name="Read", tool_input={"file_path": str(motos / "x.md")}), pin)[0]
        b, _, novo = avaliar_trava(w(CLIENTES / "cliente-novo" / "profile.md"), pin)
        assert not b and novo == "cliente-novo"  # cadastro novo: a conversa passa a ser dele
        assert avaliar_trava(sh("mkdir -p clientes/outro-novo/marca"), pin)[2] == "outro-novo"
        assert avaliar_trava(sh("echo x >> clientes/sao-jorge-motos/a.md"), pin)[0]
        assert avaliar_trava(sh(f'cp /tmp/a.md "{motos}/b.md"'), pin)[0]
        assert avaliar_trava(sh("sed -i '' 's/a/b/' clientes/sao-jorge-motos/a.md"), pin)[0]
        assert not avaliar_trava(sh("cat clientes/sao-jorge-motos/a.md > /tmp/x.md"), pin)[0]
        assert not avaliar_trava(sh("grep -r tom clientes/sao-jorge-motos/"), pin)[0]

    RAIZ, CLIENTES = original
    print("✅ autoteste do contexto.py ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
