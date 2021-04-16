<template>
    <section>
        <h1>Register</h1>
        <div>
            <label for="input_username">Username</label>
            <input type="text" id="input_username" v-model="username" placeholder="Username">
            <label for="input_password">Password</label>
            <input type="password" id="input_password" v-model="password" placeholder="****">
            <label for="input_password_conf">Password's confirmation</label>
            <input type="password" id="input_password_conf" v-model="conf_password" placeholder="****">
            <label for="input_email">Email</label>
            <input type="email" id="input_email" v-model="email" placeholder="Email">
            <input type="button" v-on:click="try_register"  id="input_register" value="Register">
        </div>
        <div>
            <router-link to="/login">Login</router-link>
        </div>
    </section>
</template>

<script>

import APIRequester from "../tools/APIRequester"
import router from "../router/router";

export default {
    name:"Register",
    data(){
        return{
          username : "",
          password : "",
          conf_password : "",
          email : "",
        }
    },
    methods:
    {
        async try_register()
        {
            if(this.password== this.conf_password)
            {
                try
                {
                    await APIRequester.getInstance().setRoute("user").setParam({"username": this.username, "password": this.password, "email": this.email, "games" : []}).post();
                    // Login successful
                    router.push({name: "Login"})
                }
                catch(error)
                {
                    // TODO : Remove and react
                    console.log(error)
                }
            }
            else
            {
                // TODO: toast with password incorrect
                console.log("password do not match")
            }
            
        }
    }

}


</script> 