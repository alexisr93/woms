<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1>Ticket Mangement</h1>
        <hr>
        <b-button to="/newticket" variant="outline-primary">New Ticket</b-button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope='col'>Issue</th>
              <th scope="col">Assigned To</th>
              <th scope="col">Submitted By</th>
              <th scope="col">Status</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(ticket, index) in tickets" :key="index">
              <td>{{ ticket.id }}</td>
              <td>{{ ticket.issue }}</td>
              <td>{{ ticket.assigned_to }}</td>
              <td>{{ ticket.submitted_by_first_name }} {{ ticket.submitted_by_last_name }}</td>
              <td>{{ ticket.status }}</td>
              <td>
                <div class="btn-group" role="group">
                  <b-button
                    variant="outline-primary"
                    v-b-modal.update-ticket-modal
                    @click="onUpdateTicket(ticket)">
                    Update
                  </b-button>
                  <b-button
                    :to="{ path: 'viewticket', query: { id: ticket.id }}"
                    variant="outline-secondary"
                    @click="onViewTicket(ticket)">
                    View
                  </b-button>
                  <b-button
                    variant="outline-danger"
                    @click="onDeleteTicket(ticket)">
                    Delete
                  </b-button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      ref="updateTicketModal"
      id="update-ticket-modal"
      title="Update"
      hide-footer>
      <b-form @submit="onSubmitUpdate" class="w-100">
      <b-form-group
        id="form-update-assigned-to-group"
        label="Assigned To:"
        label-for="form-update-assigned-to-input">
          <b-form-input
            id="form-update-assigned-to-input"
            type="text"
            v-model="updateForm.assigned_to"
            required
            placeholder="Enter name">
          </b-form-input>
        </b-form-group>
      <b-form-group
        id="form-notes-group"
        label="Notes:"
        label-for="form-notes-input">
          <b-form-textarea
            id="form-notes-input"
            type="text"
            v-model="updateForm.notes"
            required
            placeholder="Add notes once resolved">
          </b-form-textarea>
      </b-form-group>
        <b-form-group
          id="form-update-status-group"
          label="Status:">
          <b-form-radio-group id="form-radios">
            <b-form-radio v-model="updateForm.status" value="Pending">Pending</b-form-radio>
            <b-form-radio v-model="updateForm.status" value="Complete">Complete</b-form-radio>
          </b-form-radio-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="outline-primary">Submit Update</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tickets: [],
      updateForm: {
        id: '',
        assigned_to: '',
        notes: '',
        status: '',
      },
    };
  },
  methods: {
    getTickets() {
      const path = 'http://localhost:5000/tickets';
      axios.get(path)
        .then((res) => {
          this.tickets = res.data.tickets;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onUpdateTicket(ticket) {
      this.updateForm.id = ticket.id;
      this.updateForm.assigned_to = ticket.assigned_to;
      this.updateForm.notes = ticket.notes;
      this.updateForm.status = ticket.status;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.updateTicketModal.hide();

      const payload = {
        assigned_to: this.updateForm.assigned_to,
        notes: this.updateForm.notes,
        status: this.updateForm.status,
      };
      this.updateTicketDB(payload, this.updateForm.id);
    },
    updateTicketDB(payload, ticketID) {
      const path = `http://localhost:5000/tickets/${ticketID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTickets();
          this.message = 'Ticket updated!';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTickets();
        });
    },
    removeTicket(ticketID) {
      const path = `http://localhost:5000/tickets/${ticketID}`;
      axios.delete(path)
        .then(() => {
          this.getTickets();
          this.message = 'Ticket Removed!!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTickets();
        });
    },
    onDeleteTicket(ticket) {
      this.removeTicket(ticket.id);
    },
  },
  created() {
    this.getTickets();
  },
};
</script>
