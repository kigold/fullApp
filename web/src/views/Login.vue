<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div class="field">
        <label>Email</label>
        <input v-model="loginData.email" type="text" placeholder="Your user name" />
      </div>
      <div class="field">
        <label>Password</label>
        <input v-model="loginData.password" type="password" placeholder="password" />
      </div>
      <div class="field">
        <input type="submit" />
      </div>
    </form>
  </div>
</template>

<script>
import { login } from '@/helper/actionsConstants'
export default {
  data() {
    let loginData = {}
    return {
      loginData
    }
  },
  methods: {
    async login() {
      console.log("Attempting login")
      await this.$store.dispatch(login, this.loginData)
      this.$router.push({
        name: 'teams'
      })
    }
  }
}
</script>
