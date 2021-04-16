import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Home from '../views/Home.vue'
import GameViewer from '../views/GameViewer.vue'
import TestApi from '../views/TestAPI.vue'
import Logout from '../views/Logout.vue'
import E404 from '../views/E404.vue'


// Use Vue plugins
Vue.use(VueRouter)

/**
 * All routes for Toudoum App !
 */

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {
            onlyUnlogged: true
        }
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
        meta: {
            onlyUnlogged: true
        }
    },
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            onlyLogged: true
        }
    },
    {
        path: '/test',
        name: 'TestAPI',
        component: TestApi,
        meta: {
            onlyLogged: true
        }
    },
    {
        path: '/game',
        name: 'Game',
        component: GameViewer,
        props: true,
        meta: {
            onlyLogged: true
        }
    },
    {
        path: '/logout',
        name: 'Logout',
        component:  Logout,
        meta: {
            onlyLogged: true
        }
    },
    {
        path: '/404',
        name: '404',
        component:  E404,
    },
]

const router = new VueRouter({
    routes
})

function isLogged()
{
    // Not connected by login action
    if (localStorage.getItem('access') == null)
    {
        return false
    }
    return true

}

router.beforeEach((to, from, next) => {
    if (to.name == null)
    {
        next({name: "404"});
    }
    else if (to.matched.some((route) => route.meta.onlyLogged)) {
        if (!isLogged()) {
            next({ name: "Login" });
        } else {
            next();
        }
    } else if (to.matched.some((route) => route.meta.onlyUnlogged)) {
        if (isLogged()) {
            next({ name: "Home" });
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router
