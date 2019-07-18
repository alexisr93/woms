<template>
  <div>
    <h1>{{ ticketID }}</h1>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      ticketID: '',
      ticket: ''
    };
  },
  methods: {
    getTicket(ticketID) {
      const path = 'http://localhost:5000/tickets';
      axios.get(path)
        .then((res) => {
          this.ticket = res.data.tickets;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.ticketID = this.$route.query.id
    this.getTicket(ticketID);
  },
};

</script>
