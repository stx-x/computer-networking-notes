---
layout: home

hero:
  name: 计算机网络
  text: 自顶向下方法 · 全章中文译注
  tagline: 依据 Kurose & Ross 第 9 版逐节译注，保留原书全部 287 张插图与公式推导。从应用层一路走到链路层与网络安全，把自己当作在浏览器里输入网址的那个人，再一层层向下追问。
  actions:
    - theme: brand
      text: 从第 1 章读起
      link: /ch01/
    - theme: alt
      text: 看看第 8 章
      link: /ch08/

features:
  - title: 逐节对译，不是摘要
    details: 每个小节都按原书段落顺序完整译出，包括脚注式的旁白、专栏与章末复习题，不做删节式改写。
  - title: 插图与公式全部保留
    details: 287 张图按原书编号重排，所有公式用 LaTeX 重排为矢量算式，缩放不失真。
  - title: 每个协议都配一个数字
    details: 端口号、首部长度、超时门限、窗口上限——凡是能记住的数字都在正文里就地给出，末尾另附速查表。
---

<script setup>
import { withBase } from 'vitepress'
</script>

<div class="stat-strip">
  <div class="stat"><b>8</b><span>章</span></div>
  <div class="stat"><b>77</b><span>节</span></div>
  <div class="stat"><b>287</b><span>张插图</span></div>
  <div class="stat"><b>50</b><span>万字</span></div>
</div>

## 八章正文

按原书顺序排列。第 2 章之后的那一节是第 9 版删去的内容，单独保留作为补页。

<HomeChapterGrid />

## 怎么读

**第一次读**，按 1 → 8 的顺序走。自顶向下的意思不是修辞：第 2 章的 HTTP 会反复出现到第 8 章的 TLS，第 3 章的拥塞控制要靠第 4 章的队列延迟才讲得透，第 5 章的路由算法又依赖第 6 章的链路代价。

**复习**，直接从每章的「小结 + 复习题」进。每章末尾都有 R1–R2x 的完整题目，覆盖该章所有需要能一句话答上来的点。

**查数字**，用右上角搜索。端口号、窗口上限、超时门限这类东西散在正文里，各章附录有速查表。

<style>
.stat-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  margin: 56px 0 8px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  overflow: hidden;
  background: var(--vp-c-divider);
}
.stat {
  background: var(--vp-c-bg);
  padding: 22px 20px;
  display: flex;
  align-items: baseline;
  gap: 6px;
}
.stat b {
  font-size: 30px;
  font-weight: 800;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, #4f46e5, #06b6d4);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.stat span {
  font-size: 13px;
  color: var(--vp-c-text-3);
}
@media (max-width: 720px) {
  .stat-strip { grid-template-columns: repeat(2, 1fr); }
}
</style>
