/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore("user", {
  state: () => ({
    users: [],
    //
  }),
  getters: {
    getUsers() {
      return this.users;
    },
    //
  },
  actions: {
    async fetchUsers() {
      console.log("fetching users");
      const response = await axios.get(
        "http://127.0.0.1:8000/users/get_all_users"
      );
      this.users = response.data;
    },

    //
  },
});
