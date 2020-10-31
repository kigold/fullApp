import Vue from 'vue'
import VueRouter from 'vue-router'
import About from '../views/About.vue'
import Games from '../views/Games.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Teams from '../views/Teams.vue'
import Test from '../views/Test.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  /*{
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        // webpackChunkName: "about"
        '../views/About.vue')
  },*/
  {
    path: '/test',
    name: 'test',
    component: Test
  },
  {
    path: '/teams',
    name: 'teams',
    component: Teams
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/games',
    name: 'games',
    component: Games
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
