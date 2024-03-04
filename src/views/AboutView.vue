<template>
  <div class="about">
    <landing-app-bar />
    <v-container id="container" fluid>
      <blog-post-carousel />
      <v-container
        id="landingContainer"
        fluid
        style="border: 2px solid #fce4ec"
      >
        <v-row>
          <v-col cols="12">
            <v-app-bar
              flat
              class="d-flex justify-center"
              elevate-on-scroll
              color="#6A76AB"
              dark
              src="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt209db9312ce8d1fe/6364c712a803a24d15c8884d/Mbappe_Haaland_.jpg?auto=webp&format=pjpg&width=1080&quality=60"
            >
              <template v-slot:img="{ props }">
                <v-img
                  v-bind="props"
                  gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
                ></v-img>
              </template>
              <v-spacer></v-spacer>
              <v-btn class="ma-6" text> LaLiga </v-btn>
              <v-spacer></v-spacer>
              <v-btn class="ma-6" text> Bundesliga </v-btn>
              <v-spacer></v-spacer>

              <v-btn class="ma-6" text> EPL </v-btn>
              <v-spacer></v-spacer>

              <v-btn class="ma-6" text hover> Seri A </v-btn>
            </v-app-bar>
          </v-col>

          <v-col cols="6" class="mt-10" style="border: 1px solid #f5f5f5">
            <h1
              class="text-uppercase text-center text-decoration-underline button"
            >
              Featured Player
            </h1>
          </v-col>
          <v-col cols="6" class="mt-10" style="border: 1px solid #f5f5f5">
            <v-row style="border: 1px solid #f5f5f5">
              <v-col cols="12" style="border: 1px solid #f5f5f5">
                <h1
                  class="text-center text-uppercase button text-decoration-underline"
                >
                  transfer Romours
                </h1>
                hello right Lorem ipsum dolor sit, amet consectetur adipisicing
                elit. Perspiciatis nihil, praesentium qui reiciendis sint natus!
                Enim ex reiciendis omnis eos labore corrupti, expedita veritatis
                rem illum dignissimos laboriosam neque laudantium mollitia velit
                autem asperiores voluptatibus? Minima eveniet a hic accusamus
                pariatur, modi vero repellat sed sapiente ex, atque fugiat id
                accusantium, tenetur libero sit aliquam quos eaque animi enim
                quasi cum porro et! Suscipit mollitia temporibus fugiat corrupti
                sint, excepturi aspernatur aliquid amet autem eum cum id quasi
                error, unde eaque totam, quos esse consequuntur provident
                asperiores perspiciatis distinctio. Corporis aperiam vero
                ratione? Veritatis velit soluta excepturi id, hic nemo.
                <!-- Content for the top-right sub-column -->
              </v-col>
              <v-col cols="12" style="border: 1px solid #f5f5f5">
                <h1
                  class="text-center text-uppercase button text-decoration-underline"
                >
                  Player Of The Week
                </h1>
                hello subright Lorem ipsum dolor sit amet consectetur
                adipisicing elit. Placeat, cupiditate pariatur. Debitis
                perspiciatis error dolores, asperiores consectetur doloremque.
                Harum impedit quas dolores similique? Culpa sit, nulla atque,
                iure expedita in vel non ab debitis beatae, maxime libero
                quibusdam doloremque! Delectus fuga tempore reiciendis
                asperiores suscipit quisquam ipsum perferendis recusandae
                repellat libero. Voluptatibus beatae accusamus veritatis
                adipisci modi deleniti numquam nostrum incidunt dolorem minus
                blanditiis, neque nam, harum officia repellendus eveniet rem?
                Recusandae repudiandae culpa voluptatum porro nihil illo. Illo
                exercitationem qui itaque numquam quo similique nesciunt harum
                eius at iure inventore hic, ut blanditiis odit modi libero magni
                non? Velit!
                <!-- Content for the bottom-right sub-column -->
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="12" class="mt-10" style="border: 1px solid #f5f5f5">
            <h1
              class="text-uppercase text-center text-underline button text-decoration-underline font-weight-black"
            >
              Know Your Manager
            </h1>
            hello bottom Lorem ipsum dolor, sit amet consectetur adipisicing
            elit. Perferendis libero, blanditiis ad, quidem quae eos omnis
            accusantium similique, possimus voluptates ea? Similique nulla in,
            laudantium fugiat a, possimus sed laborum quos dignissimos sit omnis
            qui tenetur quasi ab maxime dolores repellendus iste adipisci odio
            ad modi corporis reiciendis excepturi. Quod ad delectus quibusdam
            qui. Molestiae praesentium laborum, expedita consequatur et odit
            labore quaerat at libero ut distinctio ipsa, odio voluptate eum
            voluptatum iusto recusandae accusamus fuga quibusdam ipsum. Quis
            qui, modi vero voluptas tempora asperiores sapiente expedita
            perferendis, illo fuga nesciunt nam, soluta dolorum sequi doloremque
            totam dignissimos unde esse?
            <!-- Content for the bottom column -->
          </v-col>
        </v-row>
      </v-container>

      <v-row class="mt-2">
        <!-- {{ blogStore.paginatedBlogs }} -->
        <v-col
          v-for="blog in blogStore.paginatedBlogs"
          :key="blog.id"
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
                  v-for="(item, i) in blog.images"
                  :key="i"
                  :src="'http://' + item.src"
                  reverse-transition="fade-transition"
                  transition="fade-transition"
                  class="carousel-item-card"
                  id="carousel-item-card"
                >
                </v-carousel-item>
              </v-carousel>
            </v-card-title>
            <v-card-subtitle class="d-flex">
              <h1 class="text-left overline mt-2 mb-2">
                <span>{{ blog.title }}</span>
              </h1>
              <!-- <v-spacer></v-spacer>
              <span class="mt-2 mb-2">
                <v-icon x-small class="mr-2"> mdi-watch </v-icon>
                30 min read</span
              > -->
            </v-card-subtitle>

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
      <v-pagination
        circle
        v-model="blogStore.page"
        :length="Math.ceil(blogStore.blogs.length / 8)"
        class="mt-6"
      >
      </v-pagination>
    </v-container>
  </div>
</template>
<script setup>
/* eslint-disable */
import { useBlogStore } from "@/store/blogStore";
import { computed, onMounted } from "vue";
import BlogPostCarousel from "@/components/BlogPostCarousel.vue";
import LandingAppBar from "@/components/LandingAppBar.vue";
// export default {
//   name: "AboutView",
//   components: {
//     LandingAppBar,
//     BlogPostCarousel,
//   },
//   data: () => ({
//     overlay: false,
//     page: 1,
//     pages: 10,
//     blogs: [
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1602674809970-89073c530b0a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1510566337590-2fc1f21d0faa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDJ8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//       {
//         title: "Blog 1",
//         content: "This is the content of blog 1",
//         date: "2021-03-21",
//         blogImages: [
//           "https://images.unsplash.com/photo-1510597026538-da2e86b8588a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=847&q=80",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//           "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
//         ],
//         owner: "John Doe",
//         ownerImage: "userImage",
//       },
//     ],
//   }),
//   methods: {
//     pagechange(page) {
//       this.page = page;
//     },
//     SingleBlogPage() {
//       console.log("SingleBlogPage");
//       this.$router.push("/blogs/:id");
//     },
//   },
// };
const components = {
  LandingAppBar,
  BlogPostCarousel,
};

const blogStore = useBlogStore();

onMounted(async () => {
  await blogStore.fetchBlogs();
  blogStore.getblogsLength;
});
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
