<template>
    <section>
        <h1>Login</h1>
        <form @submit="try_login" >
            <label for="input_username">Username</label>
            <input type="text" id="input_username" v-model="username" placeholder="Username" required>
            <label for="input_password">Password</label>
            <input type="password" id="input_password" v-model="password" placeholder="****" required>
            <input type="submit" id="input_login" value="Login">
        </form>
        <div>
            <router-link to="/register">Register</router-link>
        </div>
    </section>
</template>

<script>

import APIRequester from "../tools/APIRequester"
import router from "../router/router";

export default {
    name:"Login",
    data(){
        return{
          username : "",
          password : ""
        }
    },
    methods:
    {
        async try_login(e)
        {
            e.preventDefault();
            try
            {
                await APIRequester.getInstance().login(this.username, this.password)
                // Login successful
                router.push({name: "Home"})
            }
            catch(error)
            {
                this.$toasted.error('Username does not exist or credentials do not match', {duration: 5000})
            }
        }
    }

}


</script> 