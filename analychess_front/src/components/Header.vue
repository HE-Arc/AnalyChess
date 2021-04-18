<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <a class="navbar-brand">Analychess</a>
        <div class="d-flex flex-row-reverse navbar-collapse collapse justify-content-stretch mr-5" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                    <router-link to="/" class="nav-link">Home </router-link>
                </li>
                <li class="nav-item active">
                    <router-link to="/logout" class="nav-link"
                        >Logout</router-link
                    >
                </li>
            </ul>
        </div>
    </nav>
</template>


<script>
export default {
    name: "Header",
};
</script>
