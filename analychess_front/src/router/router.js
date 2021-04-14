import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Account from '../views/Account.vue'
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
        path: '/',
        name: 'Account',
        component: Account,
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
    else if (to.matched.some((route) => route.meta.onlyLogged))
    {
        next({ name: isLogged() ? "Account" : "Login" });
    }
    else
    {
        next();
    }
});

export default router
