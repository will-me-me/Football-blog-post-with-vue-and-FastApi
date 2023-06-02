<template>
  <div dark class="logindiv">
    <landing-app-bar />
    <v-container align="center" justify="center" class="mt-14">
      <v-row align="center" justify="center" class="mt-14">
        <v-col align="center" justify="center">
          <v-card
            flat
            class="mx-auto"
            max-width="600"
            elevation="1"
            light
            hover
          >
            <v-card-title class="d-flex mt-2">
              <h1 class="overline font-weight-bold" style="ali">LOGIN</h1>
              <v-spacer></v-spacer>
              <v-btn icon depressed disabled>
                <v-icon>mdi-account-lock-open-outline</v-icon>
              </v-btn>
            </v-card-title>
            <v-divider></v-divider>

            <v-card-text>
              <v-form class="mt-4">
                <v-text-field
                  prepend-icon="mdi-account"
                  name="name"
                  label="Name"
                  type="text"
                ></v-text-field>

                <v-text-field
                  id="password"
                  name="password"
                  label="Password"
                  prepend-icon="mdi-lock"
                  append-outer-icon="mdi-eye"
                  type="password"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-divider class="mt-4"></v-divider>
            <v-card-actions>
              <v-btn block dark> Login </v-btn>
            </v-card-actions>
            <v-divider class="mt-4"></v-divider>
            <v-card-actions class="mt-6">
              <v-btn outlined icon color="green">
                <v-icon> mdi-lock-reset </v-icon>
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn outlined icon color="blue">
                <v-icon>mdi-facebook</v-icon>
              </v-btn>
              <v-btn outlined icon color="blue">
                <v-icon>mdi-twitter</v-icon>
              </v-btn>
              <v-btn outlined icon color="red">
                <v-icon>mdi-google</v-icon>
              </v-btn>
            </v-card-actions>
            <v-divider></v-divider>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
/* eslint-disable */
import LandingAppBar from "@/components/LandingAppBar.vue";
export default {
  name: "UserLogin",
  components: {
    LandingAppBar,
  },

  data: () => ({}),
};
</script>

<style>
.logindiv {
  /*background-image: url("../assets/Vector_20180612_019.jpg");*/
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.logincontainer {
  height: 100vh;
  width: 100vw;
  opacity: 1;
  background-color: rgba(0, 0, 0, 0.9);
}
</style>
