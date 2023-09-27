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
    page: 1,
    pages: 10,
    blogsCount: 0,

    //
  }),
  getters: {
    //
    paginatedBlogs() {
      const startIndex = (this.page - 1) * 8;
      const endIndex = startIndex + 8;
      return this.blogs.slice(startIndex, endIndex);
    },
  },

  actions: {
    getblogsLength() {
      return this.blogs.length;
    },

    async fetchBlogs() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/posts/get_all_posts/"
        );
        this.blogs = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    //
  },
});
