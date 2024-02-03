<template>
  <button @click="logout" v-if="showLogoutButton">Logout</button>
  <router-view />
</template>

<script setup>
import {computed} from "vue";

const logout = () => document.cookie = 'Authorization=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
const showLogoutButton = computed(() => document.cookie.includes('Authorization'));

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  background: #eee;
}

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
