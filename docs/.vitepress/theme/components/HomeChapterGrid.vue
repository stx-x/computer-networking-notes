<script setup lang="ts">
import { withBase } from 'vitepress'
import chapters from '../../chapters.json'

const items = chapters as any[]
</script>

<template>
  <div class="ch-grid">
    <a v-for="c in items" :key="c.slug" class="ch-card" :href="withBase(`/${c.slug}/`)">
      <div class="ch-card__num">{{ c.num }}</div>
      <div class="ch-card__body">
        <h3 class="ch-card__title">{{ c.title }}</h3>
        <p class="ch-card__blurb">{{ c.blurb }}</p>
      </div>
      <div class="ch-card__meta">{{ c.count }} 节</div>
    </a>
  </div>
</template>

<style scoped>
.ch-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin: 28px 0 8px;
}
.ch-card {
  position: relative;
  display: flex;
  gap: 16px;
  padding: 22px 22px 20px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  background: var(--vp-c-bg);
  text-decoration: none !important;
  transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
}
.ch-card:hover {
  border-color: var(--vp-c-brand-2);
  transform: translateY(-2px);
  box-shadow: 0 10px 30px -12px rgba(79, 70, 229, 0.25);
}
.ch-card__num {
  font-family: var(--vp-font-family-mono);
  font-size: 22px;
  font-weight: 700;
  line-height: 1;
  background: linear-gradient(135deg, #4f46e5, #06b6d4);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  padding-top: 2px;
}
.ch-card__title {
  margin: 0;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--vp-c-text-1);
}
.ch-card__blurb {
  margin: 8px 0 0;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
}
.ch-card__meta {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 11.5px;
  font-family: var(--vp-font-family-mono);
  color: var(--vp-c-text-3);
}
@media (max-width: 720px) {
  .ch-grid {
    grid-template-columns: 1fr;
  }
}
</style>
