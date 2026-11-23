#!/usr/bin/env python3
"""Typst 数学 -> LaTeX(KaTeX)。

规则对齐 Typst 的排版行为（已用 typst 实测校对）：
  * `(a+b)/2` 的分子去掉括号；`1/(2e)` 的分母去掉括号；
  * `x^(N-1)` 的指数去掉括号，`(1-p)^(N-1)` 的底数保留括号；
  * `N L/R` 只取紧邻的 L 作分子；
  * 多字母标识符排正体（\\mathrm），希腊字母与运算符按表替换。
"""
from __future__ import annotations

import re

GREEK = {
    "alpha": r"\alpha", "beta": r"\beta", "gamma": r"\gamma", "delta": r"\delta",
    "epsilon": r"\epsilon", "zeta": r"\zeta", "eta": r"\eta", "theta": r"\theta",
    "iota": r"\iota", "kappa": r"\kappa", "lambda": r"\lambda", "mu": r"\mu",
    "nu": r"\nu", "xi": r"\xi", "pi": r"\pi", "rho": r"\rho", "sigma": r"\sigma",
    "tau": r"\tau", "upsilon": r"\upsilon", "phi": r"\phi", "chi": r"\chi",
    "psi": r"\psi", "omega": r"\omega",
    "Gamma": r"\Gamma", "Delta": r"\Delta", "Theta": r"\Theta", "Lambda": r"\Lambda",
    "Xi": r"\Xi", "Pi": r"\Pi", "Sigma": r"\Sigma", "Phi": r"\Phi", "Psi": r"\Psi",
    "Omega": r"\Omega",
}

SYMBOLS = {
    "times": r"\times ", "dot": r"\cdot ", "approx": r"\approx ", "equiv": r"\equiv ",
    "infinity": r"\infty ", "oo": r"\infty ", "dots": r"\cdots ", "sum": r"\sum ",
    "prod": r"\prod ", "sqrt": r"\sqrt ", "log": r"\log ", "ln": r"\ln ", "exp": r"\exp ",
    "min": r"\min ", "max": r"\max ", "mod": r"\bmod ", "xor": r"\oplus ",
    "quad": r"\quad ", "thin": r"\,", "in": r"\in ", "notin": r"\notin ",
    "subset": r"\subset ", "union": r"\cup ", "sect": r"\cap ",
    "prop": r"\propto ", "partial": r"\partial ", "integral": r"\int ", "lim": r"\lim ",
    "forall": r"\forall ", "exists": r"\exists ", "nabla": r"\nabla ",
    "star": r"\star ", "ell": r"\ell ", "degree": r"^\circ ", "prime": "'",
    "plus.minus": r"\pm ", "minus.plus": r"\mp ", "colon": ": ",
}

MULTI = {
    "<=": r"\le ", ">=": r"\ge ", "!=": r"\ne ", "->": r"\to ", "<-": r"\leftarrow ",
    "=>": r"\Rightarrow ", "<=>": r"\Leftrightarrow ", "<->": r"\leftrightarrow ",
    "|->": r"\mapsto ", "...": r"\cdots ",
}

BIN_OPS = {"+", "-", "=", "<", ">", r"\le ", r"\ge ", r"\ne ", r"\to ", r"\times ",
           r"\cdot ", r"\approx ", r"\in ", r"\propto ", r"\oplus ", r"\pm ", r"\equiv ",
           r"\leftrightarrow ", r"\Rightarrow ", r"\subset ", r"\cup ", r"\cap "}


def _esc(t: str) -> str:
    for a, b in [("\\", r"\textbackslash{}"), ("_", r"\_"), ("%", r"\%"), ("&", r"\&"),
                 ("#", r"\#"), ("$", r"\$"), ("{", r"\{"), ("}", r"\}")]:
        t = t.replace(a, b)
    return t


def _strip_parens(t: str) -> str:
    t = t.strip()
    if len(t) < 2 or not (t[0] == "(" and t[-1] == ")"):
        return t
    depth = 0
    for i, c in enumerate(t):
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0 and i < len(t) - 1:
                return t
    return t[1:-1]


class Tok:
    __slots__ = ("kind", "val")

    def __init__(self, kind, val):
        self.kind = kind
        self.val = val

    def __repr__(self):
        return f"{self.kind}:{self.val}"


def tokenize(s: str, texts: list[str]) -> list[Tok]:
    toks, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\" and i + 1 < n:
            toks.append(Tok("chr", "\\" + s[i + 1]))
            i += 2
            continue
        if c == "\x01":
            j = s.index("\x01", i + 1)
            toks.append(Tok("text", int(s[i + 1:j])))
            i = j + 1
            continue
        if c.isspace():
            i += 1
            continue
        if s[i:i + 3] in MULTI:
            toks.append(Tok("op", s[i:i + 3])); i += 3; continue
        if s[i:i + 2] in MULTI:
            toks.append(Tok("op", s[i:i + 2])); i += 2; continue
        if c.isdigit():
            j = i
            while j < n and (s[j].isdigit() or (s[j] == "." and j + 1 < n and s[j + 1].isdigit())):
                j += 1
            toks.append(Tok("num", s[i:j])); i = j; continue
        if c.isalpha():
            j = i
            while j < n and (s[j].isalnum() or s[j] == "."):
                j += 1
            toks.append(Tok("id", s[i:j])); i = j; continue
        if c in "([":
            toks.append(Tok("open", c)); i += 1; continue
        if c in ")]":
            toks.append(Tok("close", c)); i += 1; continue
        if c in "{}":
            toks.append(Tok("brace", c)); i += 1; continue
        if c in "^_":
            toks.append(Tok("script", c)); i += 1; continue
        if c == "/":
            toks.append(Tok("div", c)); i += 1; continue
        if c == "|":
            toks.append(Tok("bar", c)); i += 1; continue
        if c in "+-=<>,":
            toks.append(Tok("op", c)); i += 1; continue
        toks.append(Tok("chr", c)); i += 1
    return toks


class Node:
    __slots__ = ("kind", "tex")

    def __init__(self, kind, tex):
        self.kind = kind   # atom | group | op
        self.tex = tex


class Renderer:
    def __init__(self, toks, texts):
        self.t = toks
        self.texts = texts
        self.nodes: list[Node] = []
        self.bar_open = True

    # -- 单 token 转 tex
    def atom(self, tok: Tok) -> str:
        k, v = tok.kind, tok.val
        if k == "text":
            return r"\text{" + _esc(self.texts[v]) + "}"
        if k == "num":
            return v
        if k == "id":
            if v in GREEK:
                return GREEK[v]
            if v in SYMBOLS:
                return SYMBOLS[v]
            return v if len(v) == 1 else r"\mathrm{" + v + "}"
        if k == "op":
            return MULTI.get(v, v)
        if k in ("open", "close", "brace"):
            return v
        if k == "chr":
            return v
        return ""

    # -- 只读一个原子或括号组，不处理尾随上下标
    def read_single(self, i: int):
        tok = self.t[i]
        if tok.kind == "id" and tok.val == "sqrt" and i + 1 < len(self.t):
            arg, nxt, _k = self.read_single(i + 1)
            return r"\sqrt{" + _strip_parens(arg) + "}", nxt, "atom"
        if tok.kind == "open":
            close = ")" if tok.val == "(" else "]"
            depth, j = 0, i
            while j < len(self.t):
                if self.t[j].kind == "open":
                    depth += 1
                elif self.t[j].kind == "close":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            inner = Renderer(self.t[i + 1:j], self.texts).run()
            return tok.val + inner + close, j + 1, "group"
        if tok.kind == "brace" and tok.val == "{":
            depth, j = 0, i
            while j < len(self.t):
                if self.t[j].kind == "brace" and self.t[j].val == "{":
                    depth += 1
                elif self.t[j].kind == "brace" and self.t[j].val == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            inner = Renderer(self.t[i + 1:j], self.texts).run()
            return "{" + inner + "}", j + 1, "group"
        return self.atom(tok), i + 1, "atom"

    # -- 读一个「原子 + 尾随上下标」
    def read_operand(self, i: int):
        tex, nxt, kind = self.read_single(i)
        while nxt < len(self.t) and self.t[nxt].kind == "script":
            sgn = self.t[nxt].val
            arg, nxt2, _k = self.read_single(nxt + 1)
            arg = _strip_parens(arg)
            tex += ("_{" if sgn == "_" else "^{") + arg + "}"
            nxt = nxt2
        return tex, nxt, kind

    def run(self) -> str:
        i = 0
        while i < len(self.t):
            tok = self.t[i]
            if tok.kind == "div":
                if self.nodes and self.nodes[-1].kind in ("atom", "group"):
                    num = self.nodes.pop().tex
                    num = _strip_parens(num)
                else:
                    num = ""
                den, i, _ = self.read_operand(i + 1) if i + 1 < len(self.t) else ("", i + 1, "atom")
                den = _strip_parens(den)
                self.nodes.append(Node("atom", r"\frac{" + num + "}{" + den + "}"))
                continue
            if tok.kind == "script":
                sgn = tok.val
                arg, i, _ = self.read_operand(i + 1) if i + 1 < len(self.t) else ("", i + 1, "atom")
                arg = _strip_parens(arg)
                suffix = ("_{" if sgn == "_" else "^{") + arg + "}"
                if self.nodes and self.nodes[-1].kind in ("atom", "group"):
                    self.nodes[-1].tex = self.nodes[-1].tex.rstrip() + suffix
                    if self.nodes[-1].kind == "group":
                        self.nodes[-1].kind = "atom"
                else:
                    self.nodes.append(Node("atom", "{}" + suffix))
                continue
            if tok.kind == "op":
                self.nodes.append(Node("op", MULTI.get(tok.val, SYMBOLS.get(tok.val, tok.val)) or tok.val))
                i += 1
                continue
            if tok.kind == "id" and tok.val == "sqrt" and i + 1 < len(self.t):
                arg, i, _k = self.read_single(i + 1)
                self.nodes.append(Node("atom", r"\sqrt{" + _strip_parens(arg) + "}"))
                continue
            if tok.kind == "bar":
                self.nodes.append(Node("op", r"\lvert " if self.bar_open else r"\rvert "))
                self.bar_open = not self.bar_open
                i += 1
                continue
            if tok.kind == "close":
                i += 1
                continue
            tex, i, kind = self.read_operand(i)
            self.nodes.append(Node(kind, tex))
        return self.join()

    def join(self) -> str:
        out = ""
        for n in self.nodes:
            t = n.tex
            if n.kind == "op":
                if t.strip() in (",", ":"):
                    out = out.rstrip() + t.strip() + " "
                else:
                    out += " " + t.strip() + " " if t.strip() else " "
            else:
                if out and not out.endswith((" ", "{", "(")) and not t.startswith((")", "]", ",", "(")):
                    out += " "
                out += t
        res = re.sub(r"\s{2,}", " ", out).strip()
        res = res.replace("( ", "(").replace(" )", ")")
        return res


def math_to_latex(src: str) -> str:
    s = src.replace("\\/", "/")
    texts: list[str] = []
    buf, i, n = [], 0, len(s)
    while i < n:
        if s[i] == '"':
            j = s.index('"', i + 1)
            texts.append(s[i + 1:j])
            buf.append(f"\x01{len(texts) - 1}\x01")
            i = j + 1
        else:
            buf.append(s[i])
            i += 1
    toks = tokenize("".join(buf), texts)
    return Renderer(toks, texts).run()
