<template>
  <v-carousel
    dark
    height="600"
    hide-delimiter-background
    show-arrows-on-hover
    cycle
    class="opacity-carousel elevation-0"
  >
    <v-carousel-item
      v-for="(item, i) in items"
      :key="i"
      :src="item.link"
      reverse-transition="fade-transition"
      transition="fade-transition"
      height="600"
      class="carousel-item-card"
    >
      <!-- make the v-sheet transparent -->
      <!-- <v-sheet height="100%" color="transparent">
        <v-row class="fill-height ma-0" align="center" justify="center">
          <div class="display-3">
            <h1
              class="text-center white--text font-weight-bold display-1 mt-6 mb-6"
            >
              {{ item.caption }}
            </h1>
          </div>
        </v-row>
      </v-sheet> -->
    </v-carousel-item>
  </v-carousel>
</template>

<script>
/* eslint-disable */
export default {
  name: "BlogPostCarousel",
  data: () => ({
    items: [
      {
        link: require("../assets/rivalsmanArs.jpg"),
        caption: "loremp ipsum 5 lorem ipsum 5",
      },
      {
        link: "https://images.unsplash.com/photo-1602674809970-89073c530b0a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
        caption: "Image 1",
      },
      {
        link: "https://images.unsplash.com/photo-1510566337590-2fc1f21d0faa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
        caption: "Image 2",
      },
      {
        link: "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption: "Image 3",
      },
      {
        link: "https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption: "loremp ipsum 4 lorem ipsum 4",
      },
      {
        link: require("../assets/adidasBoots.jpg"),
        caption: "loremp ipsum 5 lorem ipsum 5",
      },
    ],
  }),
};
</script>

<style scoped>
.v-carousel-item__image {
  object-fit: cover;
}
.opacity-carousel .carousel-item-card {
  transition: opacity 0.3s;
  opacity: 0.7;
}

.opacity-carousel .carousel-item-card.v-enter,
.opacity-carousel .carousel-item-card.v-leave-to {
  opacity: 0;
}

.opacity-carousel .carousel-item-card.v-enter-active,
.opacity-carousel .carousel-item-card.v-leave-active {
  opacity: 1;
}
</style>
