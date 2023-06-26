<template>
  <div class="about">
    <landing-app-bar />
    <v-container id="container" fluid>
      <blog-post-carousel />
      <v-row class="mt-6">
        <v-col
          v-for="blog in blogs"
          :key="blog.title"
          cols="12"
          sm="6"
          md="4"
          lg="3"
        >
          <v-card hover outlined width="100%" class="mx-auto" flat>
            <v-card-title class="white--text">
              <v-carousel
                hide-delimiter-background
                show-arrows-on-hover
                width="100%"
                height="200"
              >
                <v-carousel-item
                  v-for="(item, i) in blog.blogImages"
                  :key="i"
                  :src="item"
                ></v-carousel-item>
              </v-carousel>
            </v-card-title>

            <v-card-text>
              {{ blog.content }}
            </v-card-text>

            <v-card-actions>
              <v-btn text outlined @click="SingleBlogPage">Read More</v-btn>
            </v-card-actions>
            <v-fade-transition>
              <v-overlay v-if="hover" absolute color="#036358">
                {{ blog.content }}
              </v-overlay>
            </v-fade-transition>
          </v-card>
        </v-col>
      </v-row>
      <v-pagination circle v-model="page" :length="pages" class="mt-6">
      </v-pagination>
    </v-container>
  </div>
</template>
<script>
/* eslint-disable */
import BlogPostCarousel from "@/components/BlogPostCarousel.vue";
import LandingAppBar from "@/components/LandingAppBar.vue";
export default {
  name: "AboutView",
  components: {
    LandingAppBar,
    BlogPostCarousel,
  },
  data: () => ({
    overlay: false,
    page: 1,
    pages: 10,
    blogs: [
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1602674809970-89073c530b0a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1510566337590-2fc1f21d0faa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDJ8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
      {
        title: "Blog 1",
        content: "This is the content of blog 1",
        date: "2021-03-21",
        blogImages: [
          "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        owner: "John Doe",
        ownerImage: "userImage",
      },
    ],
  }),
  methods: {
    pagechange(page) {
      this.page = page;
    },
    SingleBlogPage() {
      console.log("SingleBlogPage");
      this.$router.push("/blogs/:id");
    },
  },
};
</script>

<style>
.about {
  /*background-image: url("../assets/baseball3.svg");
  /*background-image: url("../assets/baseball-diamond.svg");*/
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 125vh;
  width: 100vw;
  opacity: 1;
}
#container {
  height: 100vh;
}
</style>
