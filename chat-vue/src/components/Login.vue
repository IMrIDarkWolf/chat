<template>
  <div>
    <input v-model="login" placeholder="Логин">
    <input v-model="password" placeholder="Пароль">
    <button>Войти</button>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      login: '',
      password: '',
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
