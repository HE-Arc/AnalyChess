<template>
    <section>
        <h1>Login</h1>
        <div class="row">
            <div class="col d-flex justify-content-center">
                <div style="width: 50%">
                    <img
                        src="../assets/chesspiece.svg"
                        class="card-img-top"
                        alt="chess"
                    />
                </div>
            </div>
            <div class="col-2 m-5">
                <form @submit="try_login" >
                    <label for="input_username">Username</label>
                    <input
                        type="text"
                        class="form-control"
                        id="input_username"
                        v-model="username"
                        placeholder="Username"
                        required
                    />
                    <label for="input_password" class="mt-5">Password</label>
                    <input
                        type="password"
                        class="form-control"
                        id="input_password"
                        v-model="password"
                        placeholder="****"
                        required
                    />
                    <input class="mt-5" type="submit" id="input_login" value="Login" />
                </form>
                <div class="mt-5">
                    <router-link  to="/register">Register</router-link>
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
        async try_login(e) {
            e.preventDefault();
            try {
                await APIRequester.getInstance().login(
                    this.username,
                    this.password
                );
                // Login successful
                router.push({ name: "Home" });
            } catch (error) {
                this.$toasted.error(
                    "Username does not exist or credentials do not match",
                    { duration: 5000 }
                );
            }
        },
    },
};
</script> 