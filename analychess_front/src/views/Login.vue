<template>
    <section>
        <h1>Login</h1>
        <div>
            <label for="input_username">Username</label>
            <input type="text" id="input_username" v-model="username" placeholder="Username">
            <label for="input_password">Password</label>
            <input type="password" id="input_password" v-model="password" placeholder="****">
            <input type="button" v-on:click="try_login"  id="input_login" value="Login">
        </div>
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
        async try_login()
        {
            try
            {
                await APIRequester.getInstance().login(this.username, this.password)
                // Login successful
                router.push({name: "Home"})
            }
            catch(error)
            {
                // TODO : Remove and react
                console.log(error)
            }
        }
    }

}


</script> 