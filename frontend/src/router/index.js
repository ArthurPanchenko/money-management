import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthView from '../views/AuthView.vue'
import GraphView from '../views/GraphView'

const routes = [
  {
    path: '',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/auth/',
    name: 'auth',
    component: AuthView
  },
  {
    path: '/graphs/',
    name: 'graphs',
    component: GraphView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
