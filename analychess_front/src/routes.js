import Account from './views/Account.vue';
import GameViewer from './views/GameViewer.vue';

const routes = [
    {
        path: '/account',
        name: 'account',
        component: Account,        
    },
    {
        path: '/gameViewer',
        name: 'gameViewer',
        component: GameViewer,

    },
];
export default routes;