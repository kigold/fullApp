<template>
  <div>
    <h1>Teams</h1>
    <ul>
      <li v-for="team in teams" :key="team.id">
        <Team :team="team" />
      </li>
    </ul>
  </div>
</template>

<script>
import Team from '@/components/Team.vue'
import TeamsService from '@/service/TeamsService.js'

export default {
  name: 'Teams',
  components: {
    Team
  },
  data() {
    return {
      teams: []
    }
  },
  created() {
    TeamsService.getTeams()
      .then(response => {
        console.log(response.data)
        if (response.data.has_error) {
          console.log('There was an error:' + response.data.error)
        } else {
          this.teams = response.data.data.results
        }
      })
      .catch(error => {
        console.log('There was an error:' + error)
      })
  }
}
</script>

<style></style>
