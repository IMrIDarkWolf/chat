<template>
  <div>
    <h1>Чат на vue.js</h1>
    <button v-if="!auth" @click="goLogin">Вход</button>
    <button v-else @click="logout">Выход</button>
    <room v-if="auth" @openDialog="openDialog"></room>
    <messages v-if="messages_obj.show" :id="messages_obj.id"></messages>
  </div>
</template>

<script>
import Room from '@/components/rooms/Room'
import Messages from '@/components/rooms/Messages'

export default {
  name: 'Home',
  components: {
    Room,
    Messages,
  },
  data () {
    return {
      messages_obj: {
        id: '',
        show: false,
      }
    }
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("auth_token")) {
        return true
      }
    }
  },
  methods: {
    goLogin () {
      this.$router.push({name: "login"})
    },
    logout() {
      sessionStorage.removeItem("auth_token")
      window.location = '/'
    },
    openDialog(id) {
      this.messages_obj.id = id
      this.messages_obj.show = true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
