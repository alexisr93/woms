<template>
  <div class="container">
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <h1>Login</h1>
        <hr>
        <br>
      <b-form-group>
        <b-form-input
          id="form-username-input"
          type="text"
          required
          placeholder="Username">
        </b-form-input>
      </b-form-group>
      <br>
      <b-form-group>
        <b-form-input
          id="form-password-input"
          type="text"
          required
          placeholder="Password">
        </b-form-input>
      </b-form-group>
      <br>
      <b-button
        variant="outline-primary"
        @click="">
        Login
      </b-button>
      <b-button
        variant="outline-secondary"
        @click="">
        Reset Password
      </b-button>
    </b-form>
  </div>
</template>
<script>

</script>
