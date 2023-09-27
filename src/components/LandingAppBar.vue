<template>
  <div>
    <v-app-bar color="#2962FF" id="appbar" dense outlined dark app fixed>
      <v-app-bar-nav-icon
        @click.stop="userStore.drawer = !userStore.drawer"
      ></v-app-bar-nav-icon>
      <!-- <v-app-bar-icon>
        <v-icon x-large>mdi-soccer</v-icon>
      </v-app-bar-icon> -->
      <!-- <div> -->
      <v-btn rounded text to="/" class="ma-6">Home</v-btn>
      <v-btn rounded text @click="ToBlogsPath" class="ma-6">Blogs</v-btn>
      <v-btn rounded text class="ma-6" @click="ToLoginPath">Login</v-btn>
      <v-btn rounded text class="ma-6" @click="ToCreateAccount">Sign in</v-btn>
      <v-spacer></v-spacer>
      <v-btn
        rounded
        text
        class="ma-6"
        @click="OpenblogDialog"
        v-if="userStore.userLoggedIn == true"
      >
        <v-icon small left> mdi-plus-circle </v-icon>
        Add Blog
      </v-btn>
      <!-- v-if="userStore.userLoggedIn == true" -->

      <!-- </div> -->
    </v-app-bar>
    <v-dialog persistent v-model="userStore.Addblogdialog" width="500">
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
            v-model="blogStore.title"
            type="text"
          ></v-text-field>
          <v-textarea
            color="deep-purple accent-4"
            auto-grow
            label="Content"
            rows="1"
            outlined
            v-model="blogStore.content"
            prepend-icon="mdi-book-open-page-variant"
          ></v-textarea>
          <v-file-input
            color="deep-purple accent-4"
            prepend-icon="mdi-camera"
            name="pic"
            label="media"
            type="file"
            counter
            v-model="blogStore.images"
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
          <v-btn color="blue darken-1" text outlined @click="closeDialog"
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
      v-if="userStore.showProgressBar"
      color="teal"
      buffer-value="0"
      value="5"
      stream
    ></v-progress-linear>
    <v-progress-linear
      v-if="userStore.showProgressBarreverse"
      buffer-value="55"
      color="success"
      reverse
      stream
      value="50"
    ></v-progress-linear>
    <v-navigation-drawer
      v-model="userStore.drawer"
      absolute
      bottom
      temporary
      dark
    >
      <v-list class="mt-4">
        <v-list-item class="px-14">
          <v-list-item-avatar class="">
            <v-img :src="userStore.curreUserprofile" sizes="600px"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="text-h6">
              {{ userStore.currentUser.username }}
            </v-list-item-title>
            <v-list-item-subtitle>{{
              userStore.currentUser.email
            }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list class="mt-14">
        <v-list-item v-for="(icon, i) in userStore.items" :key="i" link>
          <!-- {{ userStore.items }} -->
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

<script setup>
// import { set } from 'vue/types/umd';
/* eslint-disable */
import router from "@/router";
import { useUserStore } from "@/store/userStore";
import { useBlogStore } from "@/store/blogStore";
import { computed, onMounted } from "vue";

const userStore = useUserStore();
const blogStore = useBlogStore();

const overlay = computed(() => userStore.overlay);

const ToLoginPath = () => {
  const CurrentPath = router.currentRoute.path;
  if (CurrentPath !== "/login") {
    userStore.showProgressBar = true;
    setTimeout(() => {
      router.push("/login");
      userStore.showProgressBar = false;
    }, 1500);
  }
};
const ToCreateAccount = () => {
  const CurrentPath = router.currentRoute.path;
  if (CurrentPath !== "/register") {
    userStore.showProgressBarreverse = true;
    setTimeout(() => {
      router.push("/register");
      userStore.showProgressBarreverse = false;
    }, 1500);
  }
};

const ToBlogsPath = () => {
  const CurrentPath = router.currentRoute.path;
  if (CurrentPath !== "/blogs") {
    userStore.showProgressBarreverse = true;
    setTimeout(() => {
      router.push("/blogs");
      userStore.showProgressBarreverse = false;
    }, 1500);
  }
};
const OpenblogDialog = () => {
  userStore.Addblogdialog = true;
  userStore.showProgressBar = true;
  userStore.overlay = true;
  setTimeout(() => {
    userStore.showProgressBar = false;
    userStore.overlay = false;
  }, 1500);
};
const closeDialog = () => {
  userStore.Addblogdialog = false;
};
</script>

<style>
.v-progress-circular {
  margin: 1rem;
}
</style>
