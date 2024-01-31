<template>
  <form>
    <h1>Sign up</h1>
    <div>
      <label>First name:</label>
      <input type="text" v-model="firstName">

      <label>Last name:</label>
      <input type="text" v-model="lastName">

      <label>Email:</label>
      <input type="email" required v-model="email">

      <label>Password:</label>
      <input type="Password" required v-model="password">

      <label>Confirm password:</label>
      <input type="password" required v-model="confirmPassword">

      <div class="submit" @click.prevent="signUp">
        <button>Submit</button>
      </div>

    </div>


  </form>
</template>

<script setup>
import {ref} from "vue";

const firstName = ref('');
const lastName = ref('');
const email = ref('user@example.com');
const password = ref('passwd');
const confirmPassword = ref('passwd');

const signUp = async () => {
    await fetch('http://localhost:8000/api/v1/register', {
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
  })
}
</script>
