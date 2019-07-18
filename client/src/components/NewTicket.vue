<template>
  <div class="container">
    <div>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-issue-department-group"
          label="Type of request:"
          label-for="form-issue-department-input">
          <b-form-select
            v-model="issue_department_selected"
            :options="issue_department_options"
            placeholder="Please">
          </b-form-select>
        </b-form-group>

        <b-form-group v-if="issue_department_selected === 'Maintenence'"
          id="form-issue-type-group"
          label="Problem area:"
          label-for="form-issue-type-input">
          <b-form-select
            v-model="issue_type_selected"
            :options="issue_type_options_maintence">
          </b-form-select>
        </b-form-group>

        <b-form-group v-if="issue_department_selected === 'Technology'"
          id="form-issue-type-group"
          label="Problem area:"
          label-for="form-issue-type-input">
          <b-form-select
            v-model="issue_type_selected"
            :options="issue_type_options_technology">
          </b-form-select>
        </b-form-group>

        <b-form-group
          id="form-issue-group"
          label="Issue:"
          label-for="form-issue-input">
          <b-form-textarea
            id="form-issue-input"
            type="text"
            v-model="createTicketForm.issue"
            required
            placeholder="Describe the issue">
          </b-form-textarea>
        </b-form-group>

        <b-form-group
          id="form-previous-ticket-group">
          <b-form-checkbox-group v-model="createTicketForm.previous_ticket" id="form-checks">
            <b-form-checkbox
              value="true"
              unchecked-value="false">
              Is this related to a previous work order?
            </b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-form-group
          id="form-location-group"
          label="Location:"
          label-for="form-location-input">
          <div class="row">
            <div class='col-md-6'>
              <b-form-select
                id="form-location-site-input"
                v-model="location_site_selected"
                :options="location_site_options">
              </b-form-select>
            </div>
            <div class='col-md-6'>
              <b-form-input
                id="form-location-room-input"
                type="text"
                v-model="createTicketForm.location_room"
                required
                placeholder="Room number or other location">
              </b-form-input>
            </div>
          </div>
        </b-form-group>

        <b-form-group
          id="form-submitted-by-group"
          label="Submitted By:"
          label-for="form-submiited-by-input">
          <div class="row">
            <div class='col-md-6'>
              <b-form-input
                id="form-submitted-by-input"
                type="text"
                v-model="createTicketForm.submitted_by_first_name"
                required
                placeholder="First Name">
              </b-form-input>
            </div>
            <div class='col-md-6'>
              <b-form-input
                id="form-submitted-by-input"
                type="text"
                v-model="createTicketForm.submitted_by_last_name"
                required
                placeholder="Last Name">
              </b-form-input>
            </div>
          </div>
        </b-form-group>

        <b-form-group
          id="form-contact-info-group"
          label="Contact Information:"
          label-for="form-contact-info-input">
          <div class="row">
            <div class='col-md-6'>
              <b-form-input
                id="form-contact-email-input"
                type="text"
                v-model="createTicketForm.contact_email"
                required
                placeholder="Email">
              </b-form-input>
            </div>
            <div class='col-md-6'>
              <b-form-input
                id="form-contact-phone-input"
                type="text"
                v-model="createTicketForm.contact_phone"
                required
                placeholder="Phone Number">
              </b-form-input>
            </div>
          </div>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="outline-primary">Submit</b-button>
          <b-button type="reset" variant="outline-secondary">Reset</b-button>
        </b-button-group>

      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tickets: [],
      createTicketForm: {
        issue: '',
        previous_ticket: 'false',
        location_room: '',
        submitted_by_first_name: '',
        submitted_by_last_name: '',
        contact_email: '',
        contact_phone: '',
        assigned_to: '',
        status: '',
      },
      issue_department_selected: null,
      issue_department_options: [
        { value: null, text: 'Please select a request type.' },
        { value: 'Maintenence', text: 'Maintenence' },
        { value: 'Technology', text: 'Technology' },
      ],
      issue_type_selected: null,
      issue_type_options_technology: [
        { value: null, text: 'Please select a problem type.' },
        { value: 'New accounts', text: 'New accounts' },
        { value: 'Internet Connection', text: 'Internet Connection' },
        { value: 'Smart Board', text: 'Smart Board' },
        { value: 'PC/Laptop', text: 'PC/Laptop' },
        { value: 'Login', text: 'Login' },
      ],
      issue_type_options_maintence: [
        { value: null, text: 'Please select a problem type.' },
        { value: 'Lighting ', text: 'Lighting' },
        { value: 'Windows', text: 'Windows' },
      ],
      location_site_selected: null,
      location_site_options: [
        { value: null, text: 'Please select a location.' },
        { value: 'DPHS', text: 'DPHS' },
        { value: 'BMS', text: 'BMS' },
        { value: 'ME', text: 'ME' },
        { value: 'DPE', text: 'DPE' },
        { value: 'Other', text: 'Other' },
      ],
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
    addTicket(payload) {
      const path = 'http://localhost:5000/tickets';
      axios.post(path, payload)
        .then(() => {
          // this.getTickets();
          console.log('Saul Goodman');
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          // this.getTickets();
        });
    },
    initForm() {
      this.issue_department_selected = null;
      this.issue_type_selected = null;
      this.createTicketForm.issue = '';
      this.location_site_selected = null;
      this.createTicketForm.previous_ticket = 'false';
      this.createTicketForm.location_room = '';
      this.createTicketForm.submitted_by_first_name = '';
      this.createTicketForm.submitted_by_last_name = '';
      this.createTicketForm.contact_email = '';
      this.createTicketForm.contact_phone = '';
      this.createTicketForm.assigned_to = '';
      this.createTicketForm.status = 'Pending';
    },
    onSubmit(evt) {
      evt.preventDefault();

      const payload = {
        issue_department: this.issue_department_selected,
        issue_type: this.issue_type_selected,
        issue: this.createTicketForm.issue,
        previous_ticket: this.createTicketForm.previous_ticket,
        location_site: this.location_site_selected,
        location_room: this.createTicketForm.location_room,
        submitted_by_first_name: this.createTicketForm.submitted_by_first_name,
        submitted_by_last_name: this.createTicketForm.submitted_by_last_name,
        contact_email: this.createTicketForm.contact_email,
        contact_phone: this.createTicketForm.contact_phone,
        assigned_to: this.createTicketForm.assigned_to,
        status: 'Pending',
      };
      this.addTicket(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
  },
};
</script>
