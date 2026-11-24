import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import Figure from './components/Figure.vue'
import AsideCard from './components/AsideCard.vue'
import BoxCard from './components/BoxCard.vue'
import ChapterHero from './components/ChapterHero.vue'
import ChapterLink from './components/ChapterLink.vue'
import HomeChapterGrid from './components/HomeChapterGrid.vue'
import './style.css'

function mountSidebarToggle() {
  const KEY = 'sb-hidden'
  const root = document.documentElement
  if (new URLSearchParams(location.search).has('nosb') || localStorage.getItem(KEY) === '1') {
    root.classList.add('sb-hidden')
  }

  const icon = (dir: 'left' | 'right') =>
    `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7"
      stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">` +
    (dir === 'left'
      ? '<path d="M12 5l-5 5 5 5"/><path d="M16 4v12"/>'
      : '<path d="M8 5l5 5-5 5"/><path d="M4 4v12"/>') +
    '</svg>'

  const makeBtn = (cls: string, label: string) => {
    const b = document.createElement('button')
    b.type = 'button'
    b.className = 'sb-btn ' + cls
    b.innerHTML = icon(cls.includes('in') ? 'left' : 'right') + `<span>${label}</span>`
    b.addEventListener('click', () => {
      const hidden = root.classList.toggle('sb-hidden')
      localStorage.setItem(KEY, hidden ? '1' : '0')
    })
    return b
  }

  const attach = () => {
    if (document.querySelector('.sb-btn')) return
    document.body.appendChild(makeBtn('sb-btn--in', '收起目录'))
    document.body.appendChild(makeBtn('sb-btn--out', '目录'))
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attach)
  } else {
    attach()
  }
}

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Figure', Figure)
    app.component('AsideCard', AsideCard)
    app.component('BoxCard', BoxCard)
    app.component('ChapterHero', ChapterHero)
    app.component('ChapterLink', ChapterLink)
    app.component('HomeChapterGrid', HomeChapterGrid)

    if (typeof window !== 'undefined') {
      mountSidebarToggle()
      const bar = document.createElement('div')
      bar.className = 'reading-progress'
      const attach = () => {
        document.body.appendChild(bar)
        const update = () => {
          const el = document.documentElement
          const total = el.scrollHeight - el.clientHeight
          const p = total > 0 ? el.scrollTop / total : 0
          bar.style.transform = `scaleX(${Math.min(1, Math.max(0, p))})`
          bar.classList.toggle('is-on', el.scrollTop > 80)
        }
        update()
        window.addEventListener('scroll', update, { passive: true })
        window.addEventListener('resize', update)
      }
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', attach)
      } else {
        attach()
      }
    }
  }
} satisfies Theme
