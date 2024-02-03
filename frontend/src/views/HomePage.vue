<template>
  Home Page
</template>

<script setup>
import {onMounted, ref} from "vue";

const state = ref({
  currentUser: null
});

const getCurrentUser = async () => {
  const response = await fetch('http://localhost:8000/api/v1/user/get_current_user', {
    method: 'get',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.cookie.split('csrftoken=').slice(-1)[0].split(';')[0]
    }
  });

  return await response.json()
}
onMounted(async () => {
  state.value.currentUser = await getCurrentUser()
  console.log(state.value.currentUser)
})
</script>

<style scoped>

</style>