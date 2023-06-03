<template>
  <div>
    <landing-app-bar></landing-app-bar>
    <v-row class="mainrow" no-gutters>
      <v-col cols="6">
        <div class="account_setup">
          <v-card outlined>
            <v-card-title class="d-flex justify-center">
              <span class="headline">Create Account</span>
            </v-card-title>
            <v-card-text>
              <v-divider></v-divider>
              <v-form>
                <v-text-field
                  prepend-icon="mdi-account"
                  name="name"
                  label="Name"
                  type="text"
                ></v-text-field>
                <v-text-field
                  prepend-icon="mdi-email"
                  name="email"
                  label="Email"
                  type="email"
                ></v-text-field>
                <v-text-field
                  id="password"
                  name="password"
                  label="Password"
                  prepend-icon="mdi-lock"
                  type="password"
                ></v-text-field>
                <v-text-field
                  id="password"
                  name="Confirm Password"
                  label="Confirm Password"
                  prepend-icon="mdi-lock"
                  type="password"
                ></v-text-field>

                <v-file-input
                  prepend-icon="mdi-camera"
                  name="pic"
                  label="Profile Picture"
                  type="file"
                ></v-file-input>

                <v-textarea
                  auto-grow
                  label="Bio"
                  rows="1"
                  v-model="bio"
                  outlined
                >
                </v-textarea>
              </v-form>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-btn color="blue darken-1" text outlined>Login</v-btn>
              <v-spacer></v-spacer>
              <!-- <v-btn color="blue darken-1" text>Cancel</v-btn> -->
              <v-btn color="blue darken-1" text outlined>Create Account</v-btn>
            </v-card-actions>
          </v-card>
        </div>
      </v-col>
      <v-divider vertical></v-divider>

      <v-col cols="6">
        <div class="container_create">
          <!-- <h1 class="display-1 text-center" id="introtext">Simple Rules</h1> -->
          <!-- <h2 class="display-4 text-center" id="">
            Take The Ball Pass the Ball
          </h2> -->
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
/* eslint-disable */
import LandingAppBar from "@/components/LandingAppBar.vue";

export default {
  name: "UserCreateAccount",
  components: {
    LandingAppBar,
  },
  data: () => ({
    // bio: "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts",
    //
  }),
};
</script>

<style>
.mainrow {
  height: 100vh;
}

.container_create {
  height: 100%;
  background-image: url("../assets/204.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.1;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  color: yellowgreen;
}

.account_setup {
  height: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 1;
  background: linear-gradient(180deg, white, transparent);
  display: flex;
  justify-content: center;
  align-items: center;
}

.headline {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}

.v-card {
  width: 80%;
  max-width: 500px;
}
</style>
