import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import Figure from './components/Figure.vue'
import AsideCard from './components/AsideCard.vue'
import BoxCard from './components/BoxCard.vue'
import ChapterHero from './components/ChapterHero.vue'
import ChapterLink from './components/ChapterLink.vue'
import HomeChapterGrid from './components/HomeChapterGrid.vue'
import './style.css'

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
