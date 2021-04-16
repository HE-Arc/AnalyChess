<template>
    <section>
        <h1 v-if="success">The game has been successfully added to your account!</h1>
        <h1 v-if="!success">An error occur !</h1>
        <router-link to="/">Home</router-link>
    </section>
</template>

<script>

import APIRequester from '../tools/APIRequester'

export default {
    name:"Join",
    mounted: async function () {
        try
        {
            console.log(this.$route.params.token)
            let data = await APIRequester.getInstance().setRoute("join?token="+this.$route.params.token).get()
            console.log(data)
            this.success = true
        }
        catch(e)
        {
            console.log(e)
            this.success = false
        }
    },
    data()  
    {
        return{
            success: false
        }
    },
}

</script> 