<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>{{ name }}</h1>
    <b>{{ version }} - {{ env }}</b>
  </div>
</template>

<script>
//import Items from './components/Items.vue'

import gql from 'graphql-tag'

export default {
  name: 'App',
  apollo: {
    version: gql`
    query version {
      version
    }
    `,
    env: gql`
    query env {
      env
    }`
  },
  data() {
    return {
      info: "",
      env: "",
      name: "Vue dashboard for GraphQL backend api"
    };
  }
  /*,
  components: {
    Items
  }
  */
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
