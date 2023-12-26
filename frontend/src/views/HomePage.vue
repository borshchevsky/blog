<template>
Home Page
</template>

<script setup>
import { onMounted } from "vue";

onMounted(async () => {
  await fetch('http://localhost:8000/api/v1/auth', {
    method: 'post',
  })
})
</script>

<style scoped>

</style>