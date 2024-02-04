<template>
  <form>
    <h1>Sign in</h1>
    <div>
      <label>Email:</label>
      <input type="email" required v-model="email">
      <label>Password:</label>
      <input type="Password" required v-model="password">
      <div class="submit">
        <button @click.prevent="signIn">Submit</button>
      </div>
    </div>
    <div class="register-link">
      <p>Don't have an account yet? <strong><router-link to="/signup">Sign Up</router-link> </strong></p>
    </div>
  </form>
</template>

<script setup>
import {ref} from "vue";
import router from "@/router";
import { state } from "@/utils";

const email = ref('admin@example.com')
const password = ref('admin')

const signIn = async () => {
  const response = await fetch('http://localhost:8000/api/v1/auth', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify({
      email: email.value,
      password: password.value
    }),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.cookie.split('csrftoken=').slice(-1)[0].split(';')[0]
    }
  });

  if (response.ok) {
    const json = await response.json()
    state.value.currentUser = json['user']
    await router.push('/')
  }
}
</script>

<style scoped>
.register-link {
  font-size: 12px;
  text-align: center;
  margin-top: 50px;
}
</style>