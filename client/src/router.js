import Vue from 'vue';
import Router from 'vue-router';
import Tickets from './components/Tickets.vue';
import NewTicket from './components/NewTicket.vue';
import Login from './components/Login.vue';
import ViewTicket from './components/ViewTicket.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Tickets',
      component: Tickets,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/newticket',
      name: 'NewTicket',
      component: NewTicket,
    },
    {
      path: '/viewticket',
      name: 'ViewTicket',
      component: ViewTicket,
    },
  ],
});
