import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Account from '../views/Account.vue'
import GameViewer from '../views/GameViewer.vue'
import TestApi from '../views/TestAPI.vue'


// Use Vue plugins
Vue.use(VueRouter)

/**
 * All routes for Toudoum App !
 */
const routes = [
    {
        path: '/Login',
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
        path: '/Test',
        name: 'Account',
        component: TestApi,
        meta: {
            onlyLogged: true
        }
    },
    {
        path: '/Game',
        name: 'Account',
        component: GameViewer,
        meta: {
            onlyLogged: true
        }
    },
]

const router = new VueRouter({
    routes
})

export default router