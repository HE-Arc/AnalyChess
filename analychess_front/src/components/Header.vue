<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">Analychess</a>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <router-link to="/" class="nav-link">Home </router-link>
      </li>
      <li class="nav-item">
        <router-link to="/logout" class="nav-link" >Logout</router-link>
      </li>
    </ul>
  </div>
</nav>
</template>

<script>
export default {
  name: 'Header',
}
</script>
