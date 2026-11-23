<script setup lang="ts">
defineProps<{ caption?: string }>()
</script>

<template>
  <div class="book-box">
    <div class="book-box__body">
      <slot />
    </div>
    <p v-if="caption" class="book-box__cap">{{ caption }}</p>
  </div>
</template>

<style scoped>
.book-box {
  margin: 28px 0;
}
.book-box__body {
  padding: 18px 22px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-alt);
  font-size: 15.5px;
  line-height: 1.85;
}
.book-box__body :deep(p) {
  margin: 10px 0;
  font-size: 15.5px;
  line-height: 1.85;
}
.book-box__body :deep(p:first-child) {
  margin-top: 0;
}
.book-box__body :deep(p:last-child) {
  margin-bottom: 0;
}
.book-box__body :deep(ul),
.book-box__body :deep(ol) {
  margin: 8px 0;
}
.book-box__cap {
  margin: 10px 0 0;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--vp-c-text-3);
  text-align: center;
}
</style>
