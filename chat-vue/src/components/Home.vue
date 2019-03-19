<template>
  <div>
    <h1>Чат на vue.js</h1>
    <button @click="goLogin">Вход</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    goLogin () {
      this.$router.push({name: "login"})
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
