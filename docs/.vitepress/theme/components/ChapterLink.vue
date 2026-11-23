<script setup lang="ts">
import { withBase } from 'vitepress'

defineProps<{ href: string; num?: string; title: string }>()
</script>

<template>
  <a class="chapter-link" :href="withBase(href)">
    <span v-if="num" class="chapter-link__num">{{ num }}</span>
    <span class="chapter-link__title">{{ title }}</span>
    <svg class="chapter-link__arrow" viewBox="0 0 20 20" aria-hidden="true">
      <path d="M4 10h11M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.6"
        stroke-linecap="round" stroke-linejoin="round" />
    </svg>
  </a>
</template>

<style scoped>
.chapter-link {
  border-bottom: none !important;
  color: var(--vp-c-text-1) !important;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 15px 18px;
  margin: 0 -18px;
  border-radius: 12px;
  text-decoration: none !important;
  transition: background 0.18s ease, transform 0.18s ease;
}
.chapter-link:hover {
  background: var(--vp-c-bg-soft);
  transform: translateX(2px);
}
.chapter-link__num {
  flex: none;
  min-width: 46px;
  font-family: var(--vp-font-family-mono);
  font-size: 12.5px;
  font-weight: 500;
  color: var(--vp-c-text-3);
  padding-top: 1px;
}
.chapter-link__title {
  flex: 1;
  font-size: 15.5px;
  font-weight: 500;
  color: var(--vp-c-text-1);
  line-height: 1.5;
}
.chapter-link__arrow {
  width: 16px;
  height: 16px;
  flex: none;
  color: var(--vp-c-text-3);
  opacity: 0;
  transition: opacity 0.18s ease, transform 0.18s ease;
}
.chapter-link:hover .chapter-link__arrow {
  opacity: 1;
  transform: translateX(2px);
}
</style>
