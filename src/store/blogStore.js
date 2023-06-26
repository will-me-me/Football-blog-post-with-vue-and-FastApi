/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";

export const useBlogStore = defineStore("blog", {
  state: () => ({
    title: "",
    content: "",
    images: [],
    blog: {},
    blogs: [],

    //
  }),
  getters: {
    //
  },

  actions: {
    async fetchBlogs() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/posts/get_all_posts/"
        );
        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    },
    //
  },
});
