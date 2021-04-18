<template>
    <section class="m-5">
        <h1>You've been successfully disconnected !</h1>
        <router-link to="/login">Login</router-link>
    </section>
</template>

<script>

import APIRequester from '../tools/APIRequester'

export default {
    name:"Logout",
    mounted: async function () {
        await APIRequester.getInstance().logout()
    }
}

</script> 