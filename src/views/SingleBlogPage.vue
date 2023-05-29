<template>
  <div>
    <LandingAppBar />
    <v-container>
      <v-card hover max-width="1000px" class="mx-auto blog_card">
        <v-card-title class="d-flex mt-2">
          <h1 class="overline font-weight-bold" style="ali">
            thiis the title of the blog
          </h1>
        </v-card-title>
        <v-card-title class="">
          <v-carousel
            hide-delimiter-background
            show-arrows-on-hover
            width="100%"
            height="350"
            cycle
            progress
            progress-color="green "
          >
            <v-carousel-item
              v-for="(item, i) in 4"
              :key="i"
              :src="`https://picsum.photos/seed/${i}/1200/300`"
              reverse-transition="fade-transition"
              transition="fade-transition"
            ></v-carousel-item>
          </v-carousel>
        </v-card-title>
        <v-card-title class="d-flex mt-2">
          <h1 class="overline font-weight-bold" style="ali">
            thiis the title of the blog
          </h1>
        </v-card-title>

        <v-card-text>
          <p class="text-justify card-text">
            Lorem ipsum dolor sit amet consectetur adipisicing elit Quisquam,
            voluptatum. Quisquam, voluptatum. Quisqu Lorem ipsum dolor sit amet
            consectetur adipisicing elit. Aspernatur deleniti suscipit veritatis
            odit, quibusdam quae. Incidunt expedita repellendus vero animi at
            ducimus obcaecati itaque totam suscipit, sunt dolor? Odio quaerat
            doloremque possimus est consequuntur consequatur. Sed necessitatibus
            quisquam modi est repudiandae minus cupiditate assumenda unde
            voluptatibus, accusantium quas natus similique? Lorem ipsum dolor
            sit amet consectetur adipisicing elit. Ab impedit sed enim beatae,
            delectus ea ipsum blanditiis itaque quia quisquam facere soluta quis
            id totam. Ea reiciendis consequatur provident, aperiam sint
            architecto fugiat nemo, optio iure distinctio ipsum. Tempora ex
            possimus asperiores. Quae debitis dicta odio quod fugit suscipit
            officia ex ratione quibusdam quo ducimus maiores voluptas, minima
            laudantium praesentium. Quisquam, voluptatum. Quisquam, voluptatum.
            Quisquam, Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Sint corporis quam incidunt voluptatem soluta fugiat tempora quidem
            corrupti nobis placeat impedit cum repudiandae voluptates maxime eum
            quasi, odit obcaecati eaque sunt sapiente consequuntur quae! Maxime
            aliquid reiciendis veniam dicta aut repudiandae exercitationem iusto
            praesentium sunt? Non delectus suscipit ducimus temporibus atque
            iusto magni ullam, nisi dolores autem excepturi recusandae repellat
            ipsa doloremque sint error voluptatem! Tempore, sed delectus? Sequi
            consectetur earum quidem odio tenetur quia ratione temporibus,
            eligendi autem reiciendis? Debitis reprehenderit ea necessitatibus
            consectetur est odit, hic et optio molestias laudantium nam! Tenetur
            enim quasi molestiae totam suscipit excepturi? Lorem ipsum dolor sit
            amet consectetur adipisicing elit. Incidunt sit iure dolores
            quisquam temporibus nisi error earum corrupti optio iste! Quos nisi
            quidem aspernatur adipisci ad? Numquam officia illo eveniet possimus
            tempora ad alias quis dignissimos nulla perspiciatis accusamus amet
            distinctio reiciendis quos, assumenda saepe consequuntur error
            expedita obcaecati dolore magni placeat incidunt fuga! Laborum culpa
            et inventore fuga tempore. Voluptatibus, saepe repellat eligendi,
            officia, facere dolorum quasi iusto consequuntur quo pariatur harum
            rem reiciendis amet? Voluptate soluta animi placeat rerum officia
            mollitia eligendi temporibus reiciendis minus qui consectetur
            repellat doloremque, exercitationem quam quisquam perferendis
            provident? Iure totam sequi nulla!
          </p>
        </v-card-text>
        <v-card-actions>
          <v-btn text outlined @click="SingleBlogPage">Read More</v-btn>
          <!-- likes and dislike icons here  -->
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon color="red">mdi-heart</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-heart-off</v-icon>
          </v-btn>
          <!-- comments icon here and the number of comments -->
          <v-btn icon>
            <v-icon color="blue">mdi-comment</v-icon>
          </v-btn>
          <v-menu>
            <template v-slot:activator="{ on, attrs }">
              <v-btn icon v-bind="attrs" v-on="on">
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item>
                <v-list-item-title class="overline" @click="openDeleteDialog">
                  <v-icon color="red"> mdi-delete </v-icon>
                </v-list-item-title>
              </v-list-item>
              <v-list-item>
                <v-icon color="green"> mdi-pencil </v-icon>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-card-actions>
      </v-card>
      <v-dialog width="400" v-model="deleteDialog">
        <v-card>
          <v-card-title class="headline">Delete</v-card-title>
          <v-card-text>Are you sure you want to delete this Post?</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="deleteDialog = false">
              Cancel
            </v-btn>
            <v-btn color="blue darken-1" text @click="deleteDialog = false">
              OK
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>

<script>
/* eslint-disable */
import LandingAppBar from "@/components/LandingAppBar.vue";
export default {
  name: "SingleBlogPage",
  components: {
    LandingAppBar,
  },
  data: () => ({
    deleteDialog: false,
    page: 1,
    pages: 10,
  }),
  methods: {
    openDeleteDialog() {
      this.deleteDialog = true;
    },
  },
  //
};
</script>

<style>
.blog_card {
  border-radius: 0px;
  border: 2px solid #c21717;
}
</style>
