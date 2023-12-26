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
// import router from "@/router";

const email = ref(null)
const password = ref(null)
const signIn = async () => {
  const response = await fetch('http://localhost:8000/api/v1/auth', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify({
      email: email.value,
      password: password.value
    }),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  })

  if (response.ok) {
    response.headers.getSetCookie()
  }
}

</script>

<style scoped>
form {
  position: absolute;
  width: 420px;
  background: white;
  text-align: left;
  padding: 40px;
  border-radius: 10px;

  top: 30%;
  left: 50%;
  margin: -100px 0 0 -200px;
}

label {
  color: #aaa;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.6em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}

input {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
  outline: none !important;
}

button {
  background: #0b6dff;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
  font-weight: bold;
  font-size: 14px;
}

button:active {
  transform: translateY(2px);
}

.submit {
  text-align: center;
}
</style>