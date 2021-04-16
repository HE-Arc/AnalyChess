<template>
  <section>
    <h1>Login</h1>
    <div class="row ">
      <div class="col d-flex justify-content-center">
        <div style="width:50%; ">
          <img
            src="../assets/chesspiece.svg"
            class="card-img-top"
            alt="chess"
          />
        </div>
      </div>
      <div class="col-2 m-5">
        <div class="form-group">
          <label for="input_username">Username</label>
          <input
            type="text"
            class="form-control"
            id="input_username"
            v-model="username"
            placeholder="Username"
          />
          <label for="input_password" class="mt-5">Password</label>
          <input
            type="password"
            class="form-control"
            id="input_password"
            v-model="password"
            placeholder="****"
          />
          <input
            type="button"
            class="btn btn-secondary mt-5"
            v-on:click="try_login"
            id="input_login"
            value="Login"
          />
        </div>
      </div>

      <div class="col-2"></div>
    </div>
  </section>
</template>

<script>
import APIRequester from "../tools/APIRequester";
import router from "../router/router";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async try_login() {
      try {
        await APIRequester.getInstance().login(this.username, this.password);
        // Login successful
        router.push({ name: "Home" });
      } catch (error) {
        // TODO : Remove and react
        console.log(error);
      }
    },
  },
};
</script> 