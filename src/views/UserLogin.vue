<template>
  <div dark class="logindiv">
    <landing-app-bar />
    <v-container align="center" justify="center" class="mt-14">
      <v-row align="center" justify="center" class="mt-14">
        <v-col align="center" justify="center">
          <v-card outlined class="mx-auto" max-width="600" light color="">
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
                  prepend-icon="mdi-email"
                  :rules="userStore.emailRules"
                  v-model="userStore.email"
                  name="Email"
                  label="Email"
                  type="text"
                ></v-text-field>

                <v-text-field
                  :rules="userStore.passwordRules"
                  id="password"
                  name="password"
                  label="Password"
                  v-model="userStore.password"
                  prepend-icon="mdi-lock"
                  append-outer-icon="mdi-eye"
                  type="password"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-divider class="mt-4"></v-divider>
            <v-card-actions>
              <v-btn block dark @click="loginUser"> Login </v-btn>
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
      <v-snackbar
        rounded="pill"
        v-model="userStore.snackbar"
        top
        centered
        outlined
        color="success"
        elevation="24"
      >
        {{ userStore.message }}
      </v-snackbar>
    </v-container>
  </div>
</template>

<script setup>
/* eslint-disable */
import LandingAppBar from "@/components/LandingAppBar.vue";
import { useUserStore } from "@/store/userStore";
import { computed, onMounted } from "vue";

const components = {
  LandingAppBar,
};

const openSnackBar = () => {
  userStore.snackbar = true;
  setTimeout(() => {
    userStore.snackbar = false;
  }, 3000);
};

const userStore = useUserStore();
const loginUser = () => {
  const user = {
    email: userStore.email,
    password: userStore.password,
  };
  console.log(user);
  userStore.UserLogin(user);
  openSnackBar();
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
