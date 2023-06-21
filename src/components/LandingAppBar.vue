<template>
  <div>
    <v-app-bar color="#2962FF" id="appbar" dense outlined dark app fixed>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <!-- <v-app-bar-icon>
        <v-icon x-large>mdi-soccer</v-icon>
      </v-app-bar-icon> -->
      <!-- <div> -->
      <v-btn rounded text to="/" class="ma-6">Home</v-btn>
      <v-btn rounded text @click="ToBlogsPath" class="ma-6">Blogs</v-btn>
      <v-btn rounded text class="ma-6" @click="ToLoginPath">Login</v-btn>
      <v-btn rounded text class="ma-6" @click="ToCreateAccount">Sign in</v-btn>
      <v-spacer></v-spacer>
      <v-btn rounded text class="ma-6" @click="OpenblogDialog">
        <v-icon small left> mdi-plus-circle </v-icon>
        Add Blog
      </v-btn>
      <!-- </div> -->
    </v-app-bar>
    <v-dialog persistent v-model="Addblogdialog" width="500">
      <v-card width="600" outlined>
        <v-card-title class="d-flex justify-center">
          <span class="caption overline">Add Blog</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-text-field
            color="deep-purple accent-4"
            prepend-icon="mdi-book-open-page-variant"
            name="Title"
            label="Title"
            type="text"
          ></v-text-field>
          <v-textarea
            color="deep-purple accent-4"
            auto-grow
            label="Content"
            rows="1"
            outlined
            prepend-icon="mdi-book-open-page-variant"
          ></v-textarea>
          <v-file-input
            color="deep-purple accent-4"
            prepend-icon="mdi-camera"
            name="pic"
            label="media"
            type="file"
            chips
            filled
            multiple
            clearable
            clear-icon="mdi-close-circle-outline"
          >
            <template v-slot:selection="{ text }">
              <v-chip small label color="primary" draggable dark>
                {{ text }}
              </v-chip>
            </template>
          </v-file-input>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="blue darken-1"
            text
            outlined
            @click="Addblogdialog = false"
            >Cancel</v-btn
          >
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            outlined
            @click="Addblogdialog = false"
            >Add Blog</v-btn
          >
        </v-card-actions>
      </v-card>

      <v-overlay :value="overlay">
        <v-progress-circular
          indeterminate
          size="94"
          color="teal"
          width="7"
          height="7"
        ></v-progress-circular>
      </v-overlay>
    </v-dialog>

    <v-progress-linear
      v-if="showProgressBar"
      color="teal"
      buffer-value="0"
      value="20"
      stream
    ></v-progress-linear>
    <v-progress-linear
      v-if="showProgressBarreverse"
      buffer-value="55"
      color="success"
      reverse
      stream
      value="30"
    ></v-progress-linear>
    <v-navigation-drawer v-model="drawer" absolute bottom temporary dark>
      <v-list class="mt-4">
        <v-list-item class="px-14">
          <v-list-item-avatar class="">
            <v-img
              src="https://randomuser.me/api/portraits/women/85.jpg"
              sizes="600px"
            ></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="text-h6">
              Sandra Adams
            </v-list-item-title>
            <v-list-item-subtitle>sandra_a88@gmail.com</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list class="mt-14">
        <v-list-item v-for="(icon, i) in items" :key="i" link>
          <v-list-item-icon>
            <v-icon>{{ icon.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ icon.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <template v-slot:append>
        <div class="pa-2">
          <v-btn block> Logout </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
  </div>
</template>

<script>
// import { set } from 'vue/types/umd';
/* eslint-disable */
export default {
  components: {},
  data: () => ({
    overlay: false,
    Addblogdialog: false,
    showProgressBar: false,
    showProgressBarreverse: false,
    value: 0,
    drawer: false,
    items: [
      { title: "Home", icon: "mdi-home", link: "/" },
      { title: "Blogs", icon: "mdi-information", link: "/Blogs" },
    ],
  }),

  computed: {
    // CurrentPath() {
    //   return this.showProgressBar;
    // },
    // //
  },

  methods: {
    ToLoginPath() {
      const CurrentPath = this.$router.currentRoute.path;
      if (CurrentPath !== "/login") {
        this.showProgressBar = true;
        // this.showProgressBarreverse = true;
        setTimeout(() => {
          this.$router.push("/login");
        }, 1500);
      }
    },

    OpenblogDialog() {
      this.Addblogdialog = true;
      this.overlay = true;
      setTimeout(() => {
        this.overlay = false;
        // this.Addblogdialog = false;
      }, 1500);
    },

    ToCreateAccount() {
      const CurrentPath = this.$router.currentRoute.path;

      if (CurrentPath !== "/register") {
        this.showProgressBarreverse = true;
        setTimeout(() => {
          this.$router.push("/register");
        }, 1500);
      }
    },
    ToBlogsPath() {
      const CurrentPath = this.$router.currentRoute.path;

      if (CurrentPath !== "/blogs") {
        this.showProgressBarreverse = true;
        setTimeout(() => {
          this.$router.push("/blogs");
        }, 1500);
      }
    },

    openDrawer() {
      this.drawer = true;
    },

    //
  },
};
</script>

<style>
.v-progress-circular {
  margin: 1rem;
}
</style>
