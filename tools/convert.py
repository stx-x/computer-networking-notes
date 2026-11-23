#!/usr/bin/env python3
"""把各章 sec/*.typ 转成 VitePress Markdown。"""
from __future__ import annotations

import json
import os
import re
import shutil

from PIL import Image

from mathconv import math_to_latex

ROOT = "/Users/kk/WorkBuddy AI/网络翻译"
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(SITE, "docs")
PUB = os.path.join(DOCS, "public")

CHAPTERS = [
    ("ch01", "ch01-导论", "计算机网络与因特网", "从分组交换、排队延迟到 ISP 分层", "01"),
    ("ch02", "ch02-应用层", "应用层", "HTTP/2、DNS、CDN 与套接字编程", "02"),
    ("ch03", "ch03-运输层", "运输层", "rdt 状态机、TCP 拥塞控制与 QUIC", "03"),
    ("ch04", "ch04-网络层数据平面", "网络层：数据平面", "转发、SDN 通用转发与调度算法", "04"),
    ("ch05", "ch05-网络层控制平面", "网络层：控制平面", "LS/DV、OSPF、BGP 与 SDN 控制器", "05"),
    ("ch06", "ch06-链路层与局域网", "链路层与局域网", "CRC、多路访问、ARP、交换机与 VLAN", "06"),
    ("ch07", "ch07-无线与移动网络", "无线与移动网络", "802.11、5G RAN 与移动性管理", "07"),
    ("ch08", "ch08-计算机网络安全", "计算机网络安全", "密码学、TLS 1.3、IPsec 与防火墙", "08"),
]

CONTAINERS = {
    "example": ("example", "示例"),
    "key": ("tip", "要点"),
    "remark": ("info", "注"),
    "warn": ("warning", "注意"),
    "def": ("info", "定义"),
}

CALLS = ("fig", "figure", "eq", "example", "key", "remark", "warn", "def", "aside",
         "focus", "bin", "listing", "code", "block", "text", "v", "pagebreak",
         "heading", "import", "show", "set", "let", "raw", "box", "stack", "grid",
         "align", "table", "outline", "par", "columns", "place")


# ------------------------------------------------------------------ 工具

def find_match(s: str, i: int, oc: str, cc: str) -> int:
    """s[i] == oc，返回与之配对的 cc 的下标。跳过字符串与 '$' 片段内的括号。"""
    depth = 0
    j = i
    n = len(s)
    while j < n:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == '"':
            j += 1
            while j < n and s[j] != '"':
                if s[j] == "\\":
                    j += 1
                j += 1
            j += 1
            continue
        if c == oc:
            depth += 1
        elif c == cc:
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return -1


def split_top(s: str, sep: str = ","):
    """按顶层逗号切分（忽略括号/方括号/字符串内部）。"""
    parts, buf, depth, i, n = [], [], 0, 0, len(s)
    while i < n:
        c = s[i]
        if c == '"':
            j = i + 1
            while j < n and s[j] != '"':
                j += 2 if s[j] == "\\" else 1
            buf.append(s[i:j + 1])
            i = j + 1
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        if c == sep and depth == 0:
            parts.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(c)
        i += 1
    if buf:
        parts.append("".join(buf))
    return parts


def balanced_content(s: str) -> str:
    """去掉最外层一层 (...) 或 [...] 或 {...}。"""
    s = s.strip()
    if s[:1] in "([{" and find_match(s, 0, s[0], {"(": ")", "[": "]", "{": "}"}[s[0]]) == len(s) - 1:
        return s[1:-1]
    return s


# ------------------------------------------------------------------ 行内


def strip_lets(src: str) -> str:
    out, i = [], 0
    while True:
        m = re.search(r"^#let\b", src[i:], flags=re.M)
        if not m:
            out.append(src[i:])
            break
        start = i + m.start()
        out.append(src[i:start])
        j = start + 4
        # 函数名与参数
        if j < len(src) and src[j] == "(":
            k = find_match(src, j, "(", ")")
            j = k + 1
        # 跳过 = 与右侧表达式
        eq = src.find("=", j)
        j = eq + 1 if eq > 0 else j
        while j < len(src) and src[j] in " \t\n":
            j += 1
        if j < len(src) and (src[j].isalpha() or src[j] == "_"):
            while j < len(src) and (src[j].isalnum() or src[j] == "_"):
                j += 1
            if j < len(src) and src[j] == "(":
                k = find_match(src, j, "(", ")")
                j = k + 1
        else:
            j = src.find("\n", j)
            j = len(src) if j < 0 else j
        i = j
    return "".join(out)

def inline(s: str, ctx: dict) -> str:
    out, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c == "$":
            j = i + 1
            while j < n and s[j] != "$":
                j += 1
            tex = math_to_latex(s[i + 1:j])
            out.append("$" + tex + "$")
            i = j + 1
            continue
        if c == "#":
            name, args, body, end = read_call(s, i)
            if name is None:
                out.append(c)
                i += 1
                continue
            out.append(render_inline_call(name, args, body, ctx))
            i = end
            continue
        if c in "*_":
            # 粗体 / 斜体成对
            j = s.find(c, i + 1)
            if j > i + 1 and "\n" not in s[i:j]:
                inner = inline(s[i + 1:j], ctx)
                out.append(("**" + inner + "**") if c == "*" else ("*" + inner + "*"))
                i = j + 1
                continue
            out.append(c)
            i += 1
            continue
        if c == "\\" and i + 1 < n:
            out.append(s[i:i + 2])
            i += 2
            continue
        out.append(c)
        i += 1
    txt = "".join(out)
    txt = txt.replace("`", "`")
    return txt



def attr_text(s: str) -> str:
    """把图注/标题压成纯文本并转义，供 Vue 组件属性使用。"""
    s = re.sub(r"\$([^$]*)\$", lambda m: m.group(1), s)
    s = s.replace("**", "").replace("*", "")
    s = s.replace("`", "")
    s = re.sub(r"[ \t\n]+", " ", s).strip(" ")
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))

def read_call(s: str, i: int):
    """s[i]=='#'。返回 (name, args, body, end)。"""
    m = re.match(r"#([a-zA-Z][a-zA-Z0-9]*)", s[i:])
    if not m:
        return None, None, None, i + 1
    name = m.group(1)
    j = i + m.end()
    args = ""
    if j < len(s) and s[j] == "(":
        k = find_match(s, j, "(", ")")
        if k < 0:
            return None, None, None, i + 1
        args = s[j + 1:k]
        j = k + 1
    body = None
    if j < len(s) and s[j] == "[":
        k = find_match(s, j, "[", "]")
        if k < 0:
            return None, None, None, i + 1
        body = s[j + 1:k]
        j = k + 1
    if name not in CALLS and body is None and not args:
        return None, None, None, i + 1
    return name, args, body, j



def _block_content(args: str, body: str):
    """#block(... align(center)[$..$]) 这种内容在参数里的情况。"""
    if body is not None:
        return body
    if not args:
        return None
    k = args.find("[")
    if k < 0:
        return None
    e = find_match(args, k, "[", "]")
    if e < 0:
        return None
    return args[k + 1:e]


def _maybe_display(content: str, ctx: dict) -> str | None:
    if content and re.fullmatch(r"\s*\$[^$]+\$\s*", content):
        return "\n\n$$\n" + math_to_latex(content.strip()[1:-1]) + "\n$$\n\n"
    return None


def render_inline_call(name: str, args: str, body: str, ctx: dict) -> str:
    if name in ("text",):
        if body is not None:
            return inline(body, ctx)
        m = re.findall(r'"([^"]*)"', args or "")
        return "".join(m)
    if name == "raw":
        m = re.findall(r'"([^"]*)"', args or "")
        return "`" + "".join(m) + "`" if m else ""
    if name in ("v", "h", "pagebreak", "linebreak"):
        return ""
    if name in ("block", "box", "align", "stack", "grid", "columns"):
        content = _block_content(args, body)
        disp = _maybe_display(content, ctx)
        if disp:
            return disp
        return inline(content, ctx) if content is not None else ""
    if name == "fig":
        return render_fig(args, body, ctx)
    if name == "eq":
        return render_eq(args, body, ctx)
    if name in CONTAINERS and body is not None:
        return "\n\n:::" + CONTAINERS[name][0] + "\n" + inline(body, ctx) + "\n:::\n\n"
    if name in ("aside", "focus") and body is not None:
        title = attr_text("".join(re.findall(r'"([^"]*)"', args or "")))
        return f'\n\n<AsideCard title="{title}">\n\n{inline(body, ctx)}\n\n</AsideCard>\n\n'
    if body is not None:
        return inline(body, ctx)
    return ""


def render_eq(args: str, body: str, ctx: dict) -> str:
    src = args.strip()
    num = ""
    parts = split_top(src)
    if parts:
        m = re.search(r"\$([^$]*)\$", parts[0])
        if m:
            src = m.group(1)
        if len(parts) > 1:
            num = parts[1].strip()
    tex = math_to_latex(src)
    if num:
        tex = tex + r" \tag{" + num + "}"
    return "\n\n$$\n" + tex + "\n$$\n\n"


def render_fig(args: str, body: str, ctx: dict) -> str:
    m = re.search(r'"([^"]+\.png)"', args or "")
    cap = body if body is not None else ""
    if not cap and args:
        k = args.find("[")
        if k >= 0:
            e = find_match(args, k, "[", "]")
            if e > 0:
                cap = args[k + 1:e]
    if not m:
        return ""
    path = os.path.splitext(os.path.basename(m.group(1)))[0] + ".webp"
    cap = attr_text(inline(cap, ctx))
    return f'\n\n<Figure src="{ctx["slug"]}/{path}" caption="{cap}" />\n\n'


# ------------------------------------------------------------------ 表格

def parse_table(args: str, ctx: dict):
    """从 table(...) 的参数串里解析列数与单元格。"""
    mcols = re.search(r"columns:\s*\(", args)
    ncol = 1
    rest = args
    if mcols:
        k = find_match(args, mcols.end() - 1, "(", ")")
        cols = args[mcols.end():k]
        ncol = len(split_top(cols)) or 1
        rest = args[k + 1:]
    cells, header_mode = [], False
    i, n = 0, len(rest)
    while i < n:
        c = rest[i]
        if c == "[":
            k = find_match(rest, i, "[", "]")
            cells.append((rest[i + 1:k], header_mode))
            i = k + 1
            continue
        if c == "(" and rest[i:i + 2] in ("($", "(["):
            k = find_match(rest, i, "(", ")")
            for part in split_top(rest[i + 1:k]):
                part = part.strip()
                if part.startswith("[") and part.endswith("]"):
                    cells.append((part[1:-1], header_mode))
                elif part.startswith("$") and part.endswith("$"):
                    cells.append(("$" + part[1:-1] + "$", header_mode))
                else:
                    cells.append((part, header_mode))
            i = k + 1
            continue
        if rest.startswith("table.header", i):
            j = rest.find("(", i)
            k = find_match(rest, j, "(", ")")
            header_mode = True
            inner = rest[j + 1:k]
            # 头部只取单元格
            ii, nn = 0, len(inner)
            while ii < nn:
                if inner[ii] == "[":
                    kk = find_match(inner, ii, "[", "]")
                    cells.append((inner[ii + 1:kk], True))
                    ii = kk + 1
                    continue
                ii += 1
            header_mode = False
            i = k + 1
            continue
        if rest.startswith("table.hline", i) or rest.startswith("table.vline", i):
            j = rest.find("(", i)
            k = find_match(rest, j, "(", ")")
            i = k + 1
            continue
        i += 1
    rows, row, flags = [], [], []
    for txt, is_h in cells:
        row.append(txt)
        flags.append(is_h)
        if len(row) == ncol:
            rows.append((row, flags[0]))
            row, flags = [], []
    if row:
        rows.append((row, False))
    return ncol, rows


def emit_table(ncol: int, rows, caption: str, ctx: dict) -> str:
    if not rows:
        return ""
    def cell(t):
        t = inline(t, ctx).replace("|", r"\|").replace("\n", " ")
        return re.sub(r"\s+", " ", t).strip()

    head, body = rows[0], rows[1:]
    lines = ["| " + " | ".join(cell(c) for c in head[0]) + " |",
             "| " + " | ".join(["---"] * ncol) + " |"]
    for r, _ in body:
        r = list(r) + [""] * (ncol - len(r))
        lines.append("| " + " | ".join(cell(c) for c in r[:ncol]) + " |")
    cap = f'<p class="tbl-cap">{inline(caption, ctx)}</p>\n\n' if caption else ""
    return "\n\n" + cap + "\n".join(lines) + "\n\n"


# ------------------------------------------------------------------ 块级

def convert_blocks(src: str, ctx: dict) -> str:
    src = src.replace("\r\n", "\n")
    src = re.sub(r"^#import.*$", "", src, flags=re.M)
    src = re.sub(r"^#let .*$", "", src, flags=re.M)
    out: list[str] = []
    i, n = 0, len(src)
    para: list[str] = []
    in_list = False
    levels = [len(m.group(1)) for m in re.finditer(r"^(=+)\s", src, flags=re.M)]
    base = (min(levels) - 1) if levels else 1

    def flush():
        nonlocal in_list
        if para:
            text = "".join(para)
            para.clear()
            if text.strip():
                if in_list:
                    out.append("\n")
                    in_list = False
                out.append(render_paragraph(text, ctx))

    while i < n:
        c = src[i]
        if c == "=" and (i == 0 or src[i - 1] == "\n"):
            m = re.match(r"(={1,4})\s+(.*)", src[i:])
            if m:
                flush()
                level = len(m.group(1))
                title = inline(m.group(2).strip(), ctx)
                mdlevel = max(1, level - base)
                out.append("\n" + "#" * min(mdlevel, 6) + " " + title + "\n\n")
                i += m.end()
                continue
        if c in "-+" and (i == 0 or src[i - 1] == "\n") and src[i + 1:i + 2] == " ":
            if para and "".join(para).strip():
                flush()
            j = src.find("\n", i)
            j = n if j < 0 else j
            item = src[i + 2:j]
            out.append(("- " if c == "-" else "1. ") + inline(item.strip(), ctx) + "\n")
            in_list = True
            i = j + 1
            continue
        if c == "#":
            name, args, body, end = read_call(src, i)
            if name:
                txt = render_block_call(name, args, body, ctx)
                if txt is not None:
                    flush()
                    out.append(txt)
                    in_list = False
                    i = end
                    while i < n and src[i] == "\n":
                        i += 1
                    continue
        if c == "\n":
            nxt = src[i:].lstrip("\n")
            blanks = len(src[i:]) - len(nxt)
            if blanks >= 2:
                flush()
                out.append("\n\n")
                i += blanks
                continue
            para.append("\n")
            i += 1
            continue
        para.append(c)
        i += 1
    flush()
    text = "".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def render_paragraph(text: str, ctx: dict) -> str:
    stripped = text.strip()
    if re.fullmatch(r"\$[^$]+\$", stripped) and "\n" not in stripped:
        return "$$\n" + math_to_latex(stripped[1:-1]) + "\n$$\n\n"
    lines = [ln for ln in text.split("\n")]
    rendered = []
    for ln in lines:
        rendered.append(inline(ln, ctx) if ln.strip() else "")
    return "\n".join(rendered).strip() + "\n\n"


def render_block_call(name: str, args: str, body: str, ctx: dict):
    if name in ("import", "set", "show", "let", "outline", "par"):
        return ""
    if name == "pagebreak":
        return ""
    if name == "fig":
        return render_fig(args, body, ctx)
    if name == "eq":
        return render_eq(args, body, ctx)
    if name == "figure":
        return render_figure(args, body, ctx)
    if name in CONTAINERS and body is not None:
        kind, title = CONTAINERS[name]
        inner = convert_blocks(body, ctx)
        return f'\n\n::: {kind} {title}\n\n{inner}\n:::\n\n'
    if name in ("aside", "focus") and body is not None:
        title = attr_text("".join(re.findall(r'"([^"]*)"', args or "")))
        inner = convert_blocks(body, ctx)
        return f'\n\n<AsideCard title="{title}">\n\n{inner}\n\n</AsideCard>\n\n'
    if name == "bin":
        items = re.findall(r'"([^"]*)"', body or "")
        if not items:
            items = re.findall(r'"([^"]*)"', args or "")
        return "\n\n```text\n" + "\n".join(items) + "\n```\n\n"
    if name == "listing":
        code = (args or "").strip()
        m = re.search(r'^"((?:[^"\\]|\\.)*)"', code)
        raw = m.group(1) if m else code
        raw = raw.replace("\\n", "\n").replace('\\"', '"')
        return "\n\n```text\n" + raw + "\n```\n\n"
    if name == "code":
        raw = (body or "").strip()
        return "\n\n```text\n" + raw + "\n```\n\n"
    if name in ("block", "box", "align", "stack", "grid", "columns"):
        mt = (args or "").find("table(")
        if mt >= 0:
            k = find_match(args, mt + 5, "(", ")")
            ncol, rows = parse_table(args[mt + 6:k], ctx)
            return emit_table(ncol, rows, inline(body, ctx) if body else "", ctx)
        content = _block_content(args, body)
        if content is None:
            return None
        if "mono" in (args or "") and re.search(r'"[^"]+"', content):
            raw = re.findall(r'"([^"]*)"', content)
            if raw:
                return "\n\n```text\n" + "\n".join(raw) + "\n```\n\n"
        disp = _maybe_display(content, ctx)
        if disp:
            return disp
        return "\n\n" + convert_blocks(content, ctx) + "\n\n"
    if name == "text":
        if "table(" in (args or ""):
            k = args.find("table(")
            e = find_match(args, k + 5, "(", ")")
            ncol, rows = parse_table(args[k + 6:e], ctx)
            cap = ""
            if body:
                cap = inline(body, ctx)
            return emit_table(ncol, rows, cap, ctx)
        if body is not None:
            return "\n\n" + convert_blocks(body, ctx) + "\n\n"
    if name == "table":
        ncol, rows = parse_table(args, ctx)
        return emit_table(ncol, rows, "", ctx)
    if name == "gterm":
        body = args or ""
        pairs = re.findall(r'\(\s*"([^"]*)"\s*,\s*"([^"]*)"\s*\)', body)
        if not pairs:
            return None
        lines = ["| 英文 | 中文 |", "| --- | --- |"]
        lines += [f"| {a} | {b} |" for a, b in pairs]
        return "\n\n" + "\n".join(lines) + "\n\n"
    if name == "heading":
        return ""
    return None



def _last_bracket(s: str):
    """取字符串中最后一个顶层 [...] 的内容（figure 的正文常在 align/block 的花括号里）。"""
    best = None
    i = 0
    while i < len(s):
        if s[i] == "[":
            k = find_match(s, i, "[", "]")
            if k < 0:
                break
            best = (i, k)
            i = k + 1
        else:
            i += 1
    return s[best[0] + 1:best[1]] if best else None


def render_figure(args: str, body: str, ctx: dict) -> str:
    cap = ""
    mcap = re.search(r"caption:\s*\[", args)
    if mcap:
        k = find_match(args, mcap.end() - 1, "[", "]")
        cap = args[mcap.end():k]
    img = re.search(r'"([^"]+\.png)"', args)
    if img:
        path = os.path.splitext(os.path.basename(img.group(1)))[0] + ".webp"
        return f'\n\n<Figure src="{ctx["slug"]}/{path}" caption="{attr_text(inline(cap, ctx))}" />\n\n'
    mlist = re.search(r'listing\(\s*"((?:[^"\\]|\\.)*)"', args)
    if mlist:
        code = mlist.group(1).replace('\\n', '\n').replace('\\"', '"')
        return (f'\n\n<p class="tbl-cap">{inline(cap, ctx)}</p>\n\n'
                f"```text\n{code}\n```\n\n")

    mt = args.find("table(")
    if mt >= 0:
        k = find_match(args, mt + 5, "(", ")")
        ncol, rows = parse_table(args[mt + 6:k], ctx)
        return emit_table(ncol, rows, inline(cap, ctx), ctx)

    # 纯文本框：figure(align(left, block(...[内容]...)), caption: [..])
    content = _last_bracket(args[:mcap.start()] if mcap else args)
    if content and len(re.findall(r"[\u4e00-\u9fff]", content)) > 10:
        content = re.sub(r"(?m)^\s*set .*$", "", content)
        inner = convert_blocks(content, ctx)
        if inner.strip():
            return (f'\n\n<BoxCard caption="{attr_text(inline(cap, ctx))}">\n\n'
                    f"{inner}\n</BoxCard>\n\n")
    return ""


# ------------------------------------------------------------------ 章节

def chapter_files(dirpath: str):
    main = os.path.join(dirpath, "main.typ")
    if os.path.exists(main):
        files = re.findall(r'#include\s+"([^"]+)"', open(main).read())
        return [os.path.join(dirpath, f) for f in files]
    sec = os.path.join(dirpath, "sec")
    return [os.path.join(sec, f) for f in sorted(os.listdir(sec)) if f.endswith(".typ")]


def section_meta(path: str):
    s = open(path).read()
    m = re.search(r"^==\s+(.+)$", s, flags=re.M) or re.search(r"^=+\s+(.+)$", s, flags=re.M)
    title = m.group(1).strip() if m else os.path.basename(path)
    num = ""
    mm = re.match(r"([\d.]+)\s*", title)
    if mm:
        num = mm.group(1).strip(".")
    return title, num


def main():
    man = []
    for slug, dirname, title, blurb, num in CHAPTERS:
        d = os.path.join(ROOT, dirname)
        if not os.path.isdir(d):
            continue
        # 复制图片
        src_figs = os.path.join(d, "figs")
        dst_figs = os.path.join(PUB, "figs", slug)
        os.makedirs(dst_figs, exist_ok=True)
        if os.path.isdir(src_figs):
            for f in os.listdir(src_figs):
                if not f.endswith(".png"):
                    continue
                dst = os.path.join(dst_figs, f[:-4] + ".webp")
                if os.path.exists(dst):
                    continue
                im = Image.open(os.path.join(src_figs, f)).convert("RGB")
                w, h = im.size
                if w > 1500:
                    im = im.resize((1500, round(h * 1500 / w)), Image.LANCZOS)
                im.save(dst, "WEBP", quality=88, method=6)
        files = chapter_files(d)
        outdir = os.path.join(DOCS, slug)
        os.makedirs(outdir, exist_ok=True)
        pages = []
        for fp in files:
            stem = os.path.splitext(os.path.basename(fp))[0]
            sec_title, sec_num = section_meta(fp)
            src = strip_lets(open(fp).read())
            # 章标题（一级标题）由侧边栏承担，正文里删掉，避免和节标题抢 h1
            mtitle = re.search(r"^=\s+.*\n?", src, flags=re.M)
            if mtitle:
                src = src[:mtitle.start()] + src[mtitle.end():]
            # 若正文前有引言段，把首个 == 标题提到最前
            mfirst = re.search(r"^==\s+.*$", src, flags=re.M)
            if mfirst:
                head = src[:mfirst.start()]
                if re.search(r"[\u4e00-\u9fff]", re.sub(r"#.*", "", head)):
                    src = mfirst.group(0) + "\n\n" + head.strip() + "\n\n" + src[mfirst.end():]
            md = convert_blocks(src, {"slug": slug})
            front = (
                "---\n"
                f"title: {sec_title}\n"
                f"outline: [2, 3]\n"
                "---\n\n"
            )
            open(os.path.join(outdir, stem + ".md"), "w").write(front + md)
            pages.append((stem, sec_title))
        # 章节 index
        links = "\n".join(
            f'<ChapterLink href="/{slug}/{stem}.html" title="{attr_text(t)}" />'
            for stem, t in pages
        )
        idx = (
            "---\n"
            f"title: 第 {num} 章　{title}\n"
            "outline: false\n"
            "---\n\n"
            f'<ChapterHero num="{num}" title="{title}" blurb="{blurb}" pages="{len(pages)}" />\n\n'
            "## 本章目录\n\n" + links + "\n"
        )
        open(os.path.join(outdir, "index.md"), "w").write(idx)
        man.append({"slug": slug, "num": num, "title": title, "blurb": blurb,
                    "pages": [{"href": f"/{slug}/{s}.html", "title": t} for s, t in pages]})
        print(f"{slug}: {len(pages)} pages, {len(os.listdir(dst_figs))} figs")
    os.makedirs(os.path.join(DOCS, ".vitepress"), exist_ok=True)
    json.dump(man, open(os.path.join(DOCS, ".vitepress", "chapters.json"), "w"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
