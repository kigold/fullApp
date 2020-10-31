<template>
  <div>
    <h2>{{ team.name }}</h2>
    <h3>Id: {{ team.id }}</h3>
    <h3>Country: {{ team.country }}</h3>----------------------------------------------------
  </div>
</template>

<script>
export default {
  name: 'Team',
  props: {
    team: Object
  }
}
</script>
