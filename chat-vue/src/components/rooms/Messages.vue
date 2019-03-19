<template>
  <div class="dialog">
    <div v-for="message in messages">
      <p>
        <h2>{{ message.user.username }}</h2>
        <p>{{ message.text }}</p>
        <span>{{ message.date }}</span>
      </p>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Messages',
  props: {
    id: '',
  },
  data () {
    return {
      messages: '',
    }
  },
  created() {
    $.ajaxSetup({
       headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')},
    });
    this.loadMessages()
  },
  methods: {
    loadMessages () {
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/chat/messages/",
        type: "GET",
        data: {
          room: this.id
        },
        success: (response) => {
          this.messages = response.data
        }
      })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .dialog {
    width: 70%;
    height: 100px;
    border: 1px solid #000;
  }
</style>
