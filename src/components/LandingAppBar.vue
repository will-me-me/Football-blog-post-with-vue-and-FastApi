<template>
  <div>
    <v-app-bar app color="" id="appbar" dense elevate-on-scroll flat>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <!-- <v-app-bar-icon>
        <v-icon x-large>mdi-soccer</v-icon>
      </v-app-bar-icon> -->
      <div>
        <v-btn text to="/" class="ma-6">Home</v-btn>
        <v-btn text to="/blogs" class="ma-6">Blogs</v-btn>
        <v-btn text @click="opemLoginDialog" class="ma-6">Login</v-btn>
        <v-btn text @click="openCreateAccountDialog" class="ma-6"
          >Sign in</v-btn
        >
      </div>
    </v-app-bar>
    <!-- login dialog -->
    <v-dialog v-model="Logindialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Login</span>
        </v-card-title>

        <v-card-text>
          <v-form>
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
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="Logindialog = false">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text> Login </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- end of login dialog -->
    <!-- create account dialog -->
    <v-dialog v-model="createAccountdialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Create Account</span>
        </v-card-title>

        <v-card-text>
          <v-form>
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
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="createAccountdialog = false"
          >
            Close
          </v-btn>
          <v-btn color="blue darken-1" text> Create Account </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- drawer -->
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
/* eslint-disable */
export default {
  data: () => ({
    Logindialog: false,
    createAccountdialog: false,
    drawer: false,
    items: [
      { title: "Home", icon: "mdi-home", link: "/" },
      { title: "Blogs", icon: "mdi-information", link: "/Blogs" },
    ],
  }),

  methods: {
    openDrawer() {
      this.drawer = true;
    },
    opemLoginDialog() {
      this.Logindialog = true;
    },
    openCreateAccountDialog() {
      this.createAccountdialog = true;
    },
    //
  },
};
</script>

<style></style>
