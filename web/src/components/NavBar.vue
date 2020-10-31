<template>
  <div id="nav">
    <router-link :to="{ name: 'home' }">Home</router-link>|
    <router-link :to="{ name: 'about' }">About</router-link>|
    <router-link :to="{ name: 'teams' }">Teams</router-link>|
    <router-link :to="{ name: 'test' }">Test</router-link>|
    <router-link :to="{ name: 'login' }">Login</router-link>|
    <router-link :to="{ name: 'games' }">Games</router-link>
  </div>
</template>
