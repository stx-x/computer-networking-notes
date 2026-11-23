<script setup lang="ts">
import { withBase } from 'vitepress'

const props = defineProps<{ src: string; caption?: string }>()
const url = withBase('/figs/' + props.src)
</script>

<template>
  <figure class="book-figure">
    <img :src="url" :alt="caption" loading="lazy" />
    <figcaption v-if="caption">{{ caption }}</figcaption>
  </figure>
</template>

<style scoped>
.book-figure {
  margin: 28px 0 30px;
  text-align: center;
}
.book-figure img {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  border-radius: 10px;
  background: #fff;
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 2px 8px rgba(20, 22, 30, 0.04);
}
.book-figure figcaption {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--vp-c-text-3);
  letter-spacing: 0.01em;
}
</style>
