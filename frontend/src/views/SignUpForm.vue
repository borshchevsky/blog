<template>
  <form>
    <h1>Sign up</h1>
    <div>
      <label>First name:</label>
      <input type="text">

      <label>Last name:</label>
      <input type="text">

      <label>Email:</label>
      <input type="email" required>

      <label>Password:</label>
      <input type="Password" required>

      <label>Confirm password:</label>
      <input type="password" required>

      <div class="submit">
        <button>Submit</button>
      </div>

    </div>


  </form>
</template>

<script setup>

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