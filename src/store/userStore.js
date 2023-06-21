/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";
// import { set } from "core-js/core/dict";

const passwordMatchRule = (v) =>
  v === this.password || "Password does not match";

export const useUserStore = defineStore("user", {
  state: () => ({
    valid: true,
    users: [],
    email: "",
    password: "",
    message: "",
    snackbar: false,
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    passwordRules: [
      (v) => !!v || "Password is required",
      (v) => v.length >= 8 || "Password must be at least 8 characters",
    ],
    bio: "",
    profile_pic_url: undefined,
    confirm_password: "",
    username: "",
    showPassword: false,
    imageUrl: "",

    //
  }),
  getters: {
    getUsers() {
      return this.users;
    },
  },
  actions: {
    createImage(file) {
      const reader = new FileReader();

      reader.onload = (e) => {
        this.imageUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    onFileChange(file) {
      if (!file) {
        return;
      }
      this.createImage(file);
    },

    async fetchUsers() {
      console.log("fetching users");
      const response = await axios.get(
        "http://127.0.0.1:8000/users/get_all_users"
      );
      this.users = response.data;
    },
    async UserLogin(user) {
      user = {
        email: this.email,
        password: this.password,
      };
      console.log("logging in user");
      const response = await axios.post(
        "http://127.0.0.1:8000/users/login",
        user
      );
      console.log(response.data);
      console.log(response.data.token);

      if (response.data == "User not found") {
        this.message = "User not found";
      } else if (response.data == "Incorrect password") {
        this.message = "Incorrect password";
      } else {
        localStorage.setItem("token", response.data.token);
        ("mwehacharlse@gmail.com");

        this.message = "Login successful";
      }
    },
    async UserRegister(user) {
      // const user = {
      //   username: this.username,
      //   email: this.email,
      //   password: this.password,
      //   confirm_password: this.confirm_password,
      //   profile_pic_url: this.profile_pic_url,
      //   bio: this.bio,
      // };
      console.log("registering user");
      //  pass user as query parameters
      const response = await axios.post(
        "http://127.0.0.1:8000/users/create-user?username=" +
          user.username +
          "&email=" +
          user.email +
          "&password=" +
          user.password +
          "&confirm_password=" +
          user.confirm_password +
          "&profile_pic_url=" +
          user.profile_pic_url +
          "&bio=" +
          user.bio
      );
      console.log(response.data);
      console.log(response.data.token);
    },

    async UserLogout() {
      set(this, "email", "");
      set(this, "password", "");
      set(this, "message", "");
      set(this, "snackbar", false);
      set(this, "bio", "");
      set(this, "profilePic", "");
      set(this, "confirm_password", "");

      localStorage.removeItem("token");
      router.push("/login");
    },
  },
});
