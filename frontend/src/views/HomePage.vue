<template>
  <h1>Home Page</h1>
  <div>
    <p>{{ state.currentUser && state.currentUser.username }}</p>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { state } from "@/utils"
import router from "@/router";

onMounted(() => {
  if (!state.value.currentUser) {
    router.push('/signin')
  }
})
</script>

<style scoped>

</style>