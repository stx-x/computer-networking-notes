import { defineConfig } from 'vitepress'
import chapters from './chapters.json'

const repoBase = process.env.DOCS_BASE || '/'

const sidebar = Object.fromEntries(
  chapters.map((c: any) => [
    `/${c.slug}/`,
    [
      {
        text: `第 ${c.num} 章　${c.title}`,
        items: [{ text: '本章导读', link: `/${c.slug}/` }],
      },
      {
        text: '正文',
        items: c.pages.map((p: any) => ({ text: p.title, link: p.href })),
      },
    ],
  ])
)

export default defineConfig({
  title: '计算机网络：自顶向下方法',
  description: '《Computer Networking: A Top-Down Approach》第 9 版全章中文译注',
  base: repoBase,
  lang: 'zh-CN',
  cleanUrls: false,
  lastUpdated: false,
  head: [
    ['meta', { name: 'theme-color', content: '#4f46e5' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    [
      'link',
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap'
      }
    ]
  ],
  markdown: {
    math: true,
    lineNumbers: false
  },
  themeConfig: {
    logo: false,
    outline: { level: [2, 3], label: '本页目录' },
    nav: [
      { text: '首页', link: '/' },
      {
        text: '章节目录',
        items: chapters.map((c: any) => ({
          text: `第 ${c.num} 章　${c.title}`,
          link: `/${c.slug}/`
        }))
      },
      { text: '关于', link: '/about' }
    ],
    sidebar,
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            noResultsText: '没有找到结果',
            resetButtonTitle: '清除',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' }
          }
        }
      }
    },
    docFooter: { prev: '上一节', next: '下一节' },
    darkModeSwitchLabel: '主题',
    sidebarMenuLabel: '目录',
    returnToTopLabel: '回到顶部',
    lastUpdatedText: '最后更新',
    footer: {
      message: '内部讲义 · 仅供学习交流',
      copyright: '译注整理 · 基于 Kurose & Ross, 第 9 版'
    }
  }
})
