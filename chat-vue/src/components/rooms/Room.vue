<template>
  <div>
    <div>
      <ul>
        <li v-for="room in rooms">
          <h3 @click='openDialog(room.id)'>{{room.name}}</h3>
          {{ room.date }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Room',
  data() {
    return {
      rooms: ''
    }
  },
  created() {
    $.ajaxSetup({
        headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')},
    });
    this.loadRoom()
  },
  methods: {
    loadRoom() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/chat/rooms/",
        type: "GET",
        success: (response) => {
        this.rooms = response.data
          console.log(response)
        }
      })
    },
    openDialog(id) {
      this.$emit("openDialog", id)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  h3 {
    cursor: pointer;
  }

</style>
