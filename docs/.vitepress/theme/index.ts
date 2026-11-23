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
  }
} satisfies Theme
