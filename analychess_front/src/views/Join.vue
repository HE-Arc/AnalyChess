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
            await APIRequester.getInstance().setRoute("join?token="+this.$route.params.token).get()
            this.success = true
        }
        catch(e)
        {
            this.$toasted.error("An unexpected error's occured ! Try again or contact the administrator.", {
                duration: 3500,
            });
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