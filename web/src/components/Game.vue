<template>
  <div>
    <h2>Home User {{ game.home_user }}</h2>
    <h3>Home Team {{ game.home_team }}</h3>
    <h2>Away User {{ game.away_user }}</h2>
    <h3>Away Team {{ game.away_team }}</h3>
    ----------------------------------------------------
  </div>
</template>

<script>
export default {
  name: 'Game',
  props: {
    game: Object
  }
}
</script>
