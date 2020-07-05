<template>
  <div>
    <h1>Games</h1>
    <ul>
      <li v-for="game in games" :key="game.id">
        <Game :game="game" />
      </li>
    </ul>
  </div>
</template>

<script>
import Game from '@/components/Game.vue'
import { get_games } from '@/helper/actionsConstants'
import { mapState } from 'vuex'

export default {
  name: 'Games',
  components: {
    Game
  },
  data() {
    return {
      egames: []
    }
  },
  created() {
    this.$store.dispatch(get_games)
  },
  computed: mapState(['games'])
}
</script>

<style></style>
