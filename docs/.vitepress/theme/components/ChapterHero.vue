<script setup lang="ts">
defineProps<{ num: string; title: string; blurb?: string; pages?: string | number }>()
</script>

<template>
  <header class="chapter-hero">
    <div class="chapter-hero__num">CH. {{ num }}</div>
    <h1 class="chapter-hero__title">{{ title }}</h1>
    <p v-if="blurb" class="chapter-hero__blurb">{{ blurb }}</p>
    <div class="chapter-hero__meta">
      <span>{{ pages }} 节</span>
      <span class="dot" />
      <span>全章中文译注</span>
    </div>
  </header>
</template>

<style scoped>
.chapter-hero {
  margin: 8px 0 40px;
  padding: 44px 0 34px;
  border-bottom: 1px solid var(--vp-c-divider);
}
.chapter-hero__num {
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.18em;
  color: var(--vp-c-brand-1);
}
.chapter-hero__title {
  margin: 10px 0 0;
  padding-bottom: 0 !important;
  border-bottom: none !important;
  font-size: 44px;
  line-height: 1.2;
  font-weight: 800;
  letter-spacing: -0.03em;
  border-top: none;
}
.chapter-hero__blurb {
  margin: 14px 0 0;
  font-size: 17px;
  line-height: 1.75;
  color: var(--vp-c-text-2);
}
.chapter-hero__meta {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
  font-size: 13px;
  color: var(--vp-c-text-3);
}
.dot {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: var(--vp-c-text-3);
}
@media (max-width: 640px) {
  .chapter-hero__title {
    font-size: 32px;
  }
}
</style>
