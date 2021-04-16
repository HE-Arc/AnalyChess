<template>
    <section>
        <h1>Register</h1>
        <form @submit="try_register" >
            <label for="input_username">Username</label>
            <input type="text" id="input_username" v-model="username" placeholder="Username" required>
            <label for="input_password">Password</label>
            <input type="password" id="input_password" v-model="password" placeholder="****" required>
            <label for="input_password_conf">Password's confirmation</label>
            <input type="password" id="input_password_conf" v-model="conf_password" placeholder="****" required>
            <label for="input_email">Email</label>
            <input type="email" id="input_email" v-model="email" placeholder="Email" required>
            <input type="submit" id="input_register" value="Register">
        </form>
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
        async try_register(e)
        {
            e.preventDefault(e);
            if(this.password== this.conf_password)
            {
                try
                {
                    await APIRequester.getInstance().setRoute("user").setParam({"username": this.username, "password": this.password, "email": this.email, "games" : []}).post(false);
                    // Login successful
                    router.push({name: "Login"})
                }
                catch(error)
                {
                    // username already used
                    this.$toasted.error('Username already used', {duration: 5000})
                }
            }
            else
            {
                // toast with password incorrect
                this.$toasted.error('Password are differents !', {duration: 5000})
            }
            
        }
    }

}


</script> 