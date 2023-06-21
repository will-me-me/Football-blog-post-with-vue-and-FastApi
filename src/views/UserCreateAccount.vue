<template>
  <div>
    <landing-app-bar></landing-app-bar>
    <v-row class="mainrow" no-gutters>
      <v-col cols="6">
        <div class="account_setup">
          <v-card outlined color="" flat hover exact>
            <v-card-title class="d-flex justify-center">
              <span class="headline">Create Account</span>
            </v-card-title>
            <v-card-text>
              <v-divider></v-divider>
              <v-form lazy-validation ref="form" v-model="userStore.valid">
                <v-text-field
                  color="deep-purple accent-4"
                  prepend-icon="mdi-account"
                  name="name"
                  label="Username"
                  v-model="userStore.username"
                  type="text"
                ></v-text-field>
                <v-text-field
                  color="deep-purple accent-4"
                  prepend-icon="mdi-email"
                  name="email"
                  label="Email"
                  type="email"
                  :rules="userStore.emailRules"
                  v-model="userStore.email"
                ></v-text-field>
                <v-text-field
                  color="deep-purple accent-4"
                  hint="At least 8 characters"
                  id="password"
                  name="password"
                  label="Password"
                  required
                  prepend-icon="mdi-lock"
                  :append-icon="
                    userStore.showPassword ? 'mdi-eye' : 'mdi-eye-off'
                  "
                  :type="userStore.showPassword ? 'text' : 'password'"
                  :rules="userStore.passwordRules"
                  @click:append="
                    userStore.showPassword = !userStore.showPassword
                  "
                  v-model="userStore.password"
                ></v-text-field>
                <v-text-field
                  color="deep-purple accent-4"
                  label="Confirm Password"
                  placeholder="Confirm Password"
                  prepend-icon="mdi-lock"
                  required
                  :type="userStore.showPassword ? 'text' : 'password'"
                  @click:append="
                    userStore.showPassword = !userStore.showPassword
                  "
                  :append-icon="
                    userStore.showPassword ? 'mdi-eye' : 'mdi-eye-off'
                  "
                  v-model="userStore.confirm_password"
                  hint="At least 8 characters"
                  :rules="[
                    (v) => !!v || 'Confirm password is required',
                    (v) =>
                      v === userStore.password || 'Password does not match',
                  ]"
                ></v-text-field>

                <v-file-input
                  color="deep-purple accent-4"
                  prepend-icon="mdi-camera"
                  name="pic"
                  label="Profile Picture"
                  type="file"
                  counter
                  filled
                  dense
                  accept="image/*"
                  show-size
                  clear-icon="mdi-close-circle-outline"
                  v-model="userStore.profile_pic_url"
                  @change="userStore.onFileChange"
                >
                  <template v-slot:selection="{ text }">
                    <v-chip small label color="success ">
                      {{ text }}
                    </v-chip>
                  </template>
                </v-file-input>
                <v-img :src="userStore.imageUrl" class="ma-8" />

                <v-textarea
                  color="deep-purple accent-4"
                  auto-grow
                  label="Bio"
                  rows="1"
                  outlined
                  prepend-icon="mdi-text-box"
                  v-model="userStore.bio"
                >
                </v-textarea>
              </v-form>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-btn color="blue darken-1" text outlined>Login</v-btn>
              <v-spacer></v-spacer>
              <!-- <v-btn color="blue darken-1" text>Cancel</v-btn> -->
              <v-btn color="blue darken-1" text outlined @click="CreateAccount"
                >Create Account</v-btn
              >
            </v-card-actions>
          </v-card>
        </div>
      </v-col>
      <v-divider vertical></v-divider>
      <!-- {{ users }} -->
      <v-col cols="6">
        <div class="container_create"></div>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
/* eslint-disable */
import LandingAppBar from "@/components/LandingAppBar.vue";
import { useUserStore } from "@/store/userStore";
import { computed, onMounted } from "vue";

// register the componet landing app bar
const components = {
  LandingAppBar,
};
const userStore = useUserStore();
const users = computed(() => userStore.getUsers);

const CreateAccount = () => {
  // alert("Create Account");
  const user = {
    username: userStore.username,
    email: userStore.email,
    password: userStore.password,
    confirm_password: userStore.confirm_password,
    profile_pic_url: userStore.profile_pic_url,
    bio: userStore.bio,
  };
  // pass user as query paramerter
  userStore.UserRegister(user);
  console.log(user);
};

// console.log(users);
onMounted(async () => {
  await userStore.fetchUsers();
});
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
