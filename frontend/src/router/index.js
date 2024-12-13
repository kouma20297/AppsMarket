import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Aboutus from '../views/Aboutus.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  // 他のルートをここに追加
  {
    path: '/aboutus',
    name: 'Aboutus',
    component: Aboutus,


  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
