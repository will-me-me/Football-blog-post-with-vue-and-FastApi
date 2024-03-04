/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";
// import { useRoute } from "vue-router";
// import { useRouter } from "vue-router";

export const useUserStore = defineStore("user", {
  state: () => ({
    valid: false,
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
    profile_pic_url: "",
    confirm_password: "",
    username: "",
    showPassword: false,
    imageUrl: "",
    userLoggedIn: false,

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
    currentUser: {},
    curreUserprofile: null,

    //
  }),
  getters: {
    getUsers() {
      return this.users;
    },
    validForm() {
      return (
        this.email != "" &&
        this.password != "" &&
        this.confirm_password != "" &&
        this.bio != "" &&
        this.username != ""
      );
    },
    checkIfLoggedIn() {
      return this.userLoggedIn;
    },
  },
  actions: {
    openDrawer() {
      this.drawer = true;
    },
    onFileReadCompleted(file) {
      this.profile_pic_url = file;
    },
    createImage(file) {
      const reader = new FileReader();

      reader.onload = (e) => {
        this.onFileReadCompleted(file);
      };
      reader.readAsDataURL(file);
    },
    onFileChange(event) {
      const file = event.target.files[0];

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
    parseJwt(token) {
      try {
        return JSON.parse(atob(token.split(".")[1]));
      } catch (e) {
        return null;
      }
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
        this.message = "Login successful";
        this.snackbar = true;
        localStorage.setItem("token", response.data.token);
        this.userLoggedIn = true;
        router.push("/blogs");
        const currentUser = this.parseJwt(response.data.token);
        console.log(currentUser);
        this.currentUser = currentUser;
        console.log(this.currentUser);
        const profile_pic_url = this.currentUser.profile_pic_url[0];
        console.log(profile_pic_url);
        this.curreUserprofile = profile_pic_url;
      }
    },
    async UserRegister(formData) {
      try {
        const response = await axios.post(
          `http://127.0.0.1:8000/users/create-user?username=${this.username}&email=${this.email}&password=${this.password}&confirm_password=${this.confirm_password}&bio=${this.bio}`,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
              accept: "application/json",
            },
          }
        );
      } catch (error) {
        console.error(error);
        if (error.response) {
          console.error("Response data:", error.response.data);
          console.error("Response status:", error.response.status);
          console.error("Response headers:", error.response.headers);
        }
      }
    },

    clearInputs() {
      this.email = "";
      this.password = "";
      this.confirm_password = "";
      this.bio = "";
      this.username = "";
      this.profile_pic_url = "";
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
