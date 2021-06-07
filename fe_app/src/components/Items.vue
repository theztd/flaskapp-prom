<template>
  <div id="app">
    <ul>
    <div v-for="person in contributors" :key="person.name">
      <li><b>{{ person.name }}</b> - {{ person.link }}</li>
    </div>
    </ul>
  </div>
</template>




<script>

import gql from 'graphql-tag'


export default {
  name: 'Contributors',
  props: {
    contributors: {}
  },
  apollo: {
    users: gql`
    query contributors {
      contributors: users (size:10) {
        name
        age
      }
    }
    `
  }
}
</script>





<style scoped>
ul {
  list-style-type: none;
  padding: 30;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>