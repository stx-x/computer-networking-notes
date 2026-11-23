<script setup lang="ts">
defineProps<{ title?: string }>()
</script>

<template>
  <aside class="aside-card">
    <div class="aside-card__head">
      <span class="aside-card__dot" />
      <span class="aside-card__title">{{ title || '专栏' }}</span>
    </div>
    <div class="aside-card__body">
      <slot />
    </div>
  </aside>
</template>

<style scoped>
.aside-card {
  position: relative;
  margin: 30px 0;
  padding: 1px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(79, 70, 229, 0.5), rgba(6, 182, 212, 0.35));
}
.aside-card__head {
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 14px 20px 0;
  background: var(--vp-c-bg);
  border-radius: 15px 15px 0 0;
}
.aside-card__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: linear-gradient(135deg, #4f46e5, #06b6d4);
}
.aside-card__title {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--vp-c-text-2);
}
.aside-card__body {
  padding: 4px 20px 16px;
  background: var(--vp-c-bg);
  border-radius: 0 0 15px 15px;
  font-size: 15.5px;
  line-height: 1.85;
  color: var(--vp-c-text-1);
}
.aside-card__body :deep(p) {
  margin: 10px 0;
  font-size: 15.5px;
  line-height: 1.85;
}
.aside-card__body :deep(p:first-child) {
  margin-top: 2px;
}
.aside-card__body :deep(figure) {
  margin: 16px 0;
}
</style>
