<template>
  <div dark class="logindiv">
    <landing-app-bar />
    <v-container
      align="center"
      justify="center"
      class="mt-14"
      id="particles-js"
    >
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
                  :append-icon="
                    userStore.showPassword ? 'mdi-eye' : 'mdi-eye-off'
                  "
                  :type="userStore.showPassword ? 'text' : 'password'"
                  @click:append="
                    userStore.showPassword = !userStore.showPassword
                  "
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-divider class="mt-4"></v-divider>
            <v-card-actions>
              <v-btn block dark @click="loginUser"> Login </v-btn>
            </v-card-actions>
            <v-divider class="mt-4"></v-divider>
            <v-card-actions class="mt-6">
              <v-tooltip bottom color="green" class="mt-1">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn outlined icon color="green" v-bind="attrs" v-on="on">
                    <v-icon> mdi-lock-reset </v-icon>
                  </v-btn>
                </template>
                <span>Forgot Password</span>
              </v-tooltip>
              <v-spacer></v-spacer>
              <v-tooltip bottom color="blue" class="mt-1">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    outlined
                    icon
                    color="blue"
                    v-bind="attrs"
                    v-on="on"
                    class="ma-1"
                  >
                    <v-icon>mdi-facebook</v-icon>
                  </v-btn>
                </template>
                <span class="caption">Login With Facebook</span>
              </v-tooltip>
              <v-tooltip bottom color="blue" class="mt-1">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    outlined
                    icon
                    color="blue"
                    v-bind="attrs"
                    v-on="on"
                    class="ma-1"
                  >
                    <v-icon>mdi-twitter</v-icon>
                  </v-btn>
                </template>
                <span class="caption">Login With Twitter</span>
              </v-tooltip>
              <v-tooltip bottom color="red" class="mt-1">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    outlined
                    icon
                    color="red"
                    v-bind="attrs"
                    v-on="on"
                    class="ma-1"
                  >
                    <v-icon>mdi-google</v-icon>
                  </v-btn>
                </template>
                <span class="caption">Login With Google</span>
              </v-tooltip>
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
import { useBlogStore } from "@/store/blogStore";
import { computed, onMounted } from "vue";
import particlesJS from "particles.js";

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

const blogStore = useBlogStore();
const getBlogs = () => {
  blogStore.fetchBlogs();
};

onMounted(() => {
  getBlogs();
  particlesJS("particles-js", {
    particles: {
      number: {
        value: 380,
        density: {
          enable: true,
          value_area: 800,
        },
      },
      color: {
        value: "#ffffff",
      },
      shape: {
        type: "circle",
        stroke: {
          width: 0,
          color: "#000000",
        },
        polygon: {
          nb_sides: 5,
        },
        image: {
          src: "img/github.svg",
          width: 100,
          height: 100,
        },
      },
      opacity: {
        value: 0.5,
        random: false,
        anim: {
          enable: false,
          speed: 1,
          opacity_min: 0.1,
          sync: false,
        },
      },
      size: {
        value: 3,
        random: true,
        anim: {
          enable: false,
          speed: 40,
          size_min: 0.1,
          sync: false,
        },
      },
      line_linked: {
        enable: true,
        distance: 150,
        color: "#ffffff",
        opacity: 0.4,
        width: 1,
      },
      move: {
        enable: true,
        speed: 6,
        direction: "none",
        random: false,
        straight: false,
        out_mode: "out",
        bounce: false,
        attract: {
          enable: false,
          rotateX: 600,
          rotateY: 1200,
        },
      },
    },
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: {
          enable: true,
          mode: "grab",
        },
        onclick: {
          enable: true,
          mode: "push",
        },
        resize: true,
      },
      modes: {
        grab: {
          distance: 140,
          line_linked: {
            opacity: 1,
          },
        },
        bubble: {
          distance: 400,
          size: 40,
          duration: 2,
          opacity: 8,
          speed: 3,
        },
        repulse: {
          distance: 200,
          duration: 0.4,
        },
        push: {
          particles_nb: 4,
        },
        remove: {
          particles_nb: 2,
        },
      },
    },
    retina_detect: true,
  });
  // particlesJS("particles-js", {
  //   // Configuration options for particles.js
  //   // ...

  //   particle: {
  //     color: "#fff",
  //     shape: "circle",
  //     opacity: 1,
  //     size: 4,
  //     size_random: true,
  //     nb: 150,
  //     line_linked: {
  //       enable_auto: true,
  //       distance: 100,
  //       color: "#fff",
  //       opacity: 1,
  //       width: 1,
  //       condensed_mode: {
  //         enable: false,
  //         rotateX: 600,
  //         rotateY: 600,
  //       },
  //     },
  //     anim: {
  //       enable: true,
  //       speed: 1,
  //     },
  //   },
  // });
});
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
