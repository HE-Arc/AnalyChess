<template>
  <div id="root">
    <template>
      <account/>
    </template>
  </div>
</template>
<script>  

import Account from './views/Account.vue';


export default {
  components:{
  Account,
  },
    name: "App",
  };
</script>
