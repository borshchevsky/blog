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


  </form>
</template>

<script setup>
import {ref} from "vue";

const email = ref('admin@example.com')
const password = ref('admin')

const signIn = async () => {
  await fetch('http://localhost:8000/api/v1/auth', {
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
}
</script>
