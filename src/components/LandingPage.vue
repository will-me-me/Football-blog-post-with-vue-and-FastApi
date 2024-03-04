<template>
  <div class="landingpage">
    <landing-app-bar />
    <div id="overlaydiv" class="rounded-lg">
      <h1 class="display-1 text-center" id="introtext">Simple Rules</h1>
      <h2 class="display-4 text-center" id="introphrase">
        Take The Ball, Pass the Ball.
      </h2>
      <div class="d-flex justify-center mt-12">
        <v-spacer></v-spacer>

        <v-btn
          rounded
          :loading="loading"
          :disabled="loading"
          @click="loader = 'loading'"
          color="primary"
          large
          class="ma-4 d-flex justify-center"
        >
          <v-icon left small>mdi-book</v-icon>
          blogs
        </v-btn>
        <v-spacer></v-spacer>

        <v-btn
          rounded
          large
          color="yellow darken-2"
          class="ma-4 d-flex justify-center"
        >
          <v-icon left small>mdi-account-plus</v-icon>

          Sign Up
        </v-btn>
        <v-spacer></v-spacer>

        <v-btn
          rounded
          large
          color="green darken-1"
          class="ma-4 d-flex justify-center"
        >
          <v-icon left small>mdi-login</v-icon>
          Login
        </v-btn>
        <v-spacer></v-spacer>
      </div>
      <div class="mt-8">
        <v-icon x-large color="green" size="10">
          mdi-arrow-down-bold-outline
        </v-icon>
        <v-icon x-large color="red" size="10">
          mdi-arrow-up-bold-outline
        </v-icon>
      </div>
      <div>
        <h1 class="display-1 text-center" id="abouttext">
          Discover captivating stories about legendary players, iconic moments,
          and the rich history of football clubs around the globe. Immerse
          yourself in the drama, excitement, and emotions that make football the
          most popular sport in the world.
        </h1>
      </div>
    </div>

    <div
      style="
        background-image: url('https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt209db9312ce8d1fe/6364c712a803a24d15c8884d/Mbappe_Haaland_.jpg?auto=webp&format=pjpg&width=1080&quality=60');
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        height: 100vh;
        width: 100vw;
        opacity: 0.6;
        background-color: rgba(0, 0, 0, 0.9);
      "
    >
      <h1 class="text-center justify-center">All in Safe hands</h1>
    </div>

    <div id="carusel_div">
      <v-container>
        <h1 class="display-1 text-center" id="resultstext">Results</h1>
        <carousel-3d :autoplay="true" :autoplay-timeout="1000" class="mt-4">
          <!-- Add your slides here -->
          <slide v-for="(game, i) in games" :key="game.id" :index="i">
            <v-card width="360" height="270" hover outlined color="transparent">
              <v-card-title class="d-flex justify-center">
                <h1 class="overline">{{ game.hometeam }}</h1>
                <v-spacer></v-spacer>
                <h1 class="overline">vs</h1>
                <v-spacer></v-spacer>
                <h1 class="overline">{{ game.awayteam }}</h1>
              </v-card-title>
              <v-divider></v-divider>
              <v-card-text class="d-flex">
                <v-avatar size="56">
                  <v-img
                    contain
                    :src="game.hometeamlogo"
                    alt="image"
                    aspect-ratio="1"
                    lazy-src="game.hometeamlogo"
                    class="circular-image"
                  ></v-img>
                </v-avatar>
                <v-spacer></v-spacer>
                <v-avatar size="56">
                  <v-img
                    contain
                    :src="game.awayteamlogo"
                    alt="image"
                    aspect-ratio="1"
                    lazy-src="game.awayteamlogo"
                    class="circular-image"
                  ></v-img>
                </v-avatar>
              </v-card-text>
              <v-card-text class="d-flex justify-center">
                <p class="overline font-weight-black title">
                  {{ game.homescore }} - {{ game.awayscore }}
                </p>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
                <p class="overline font-weight-black">{{ game.stadium }}</p>
                <v-spacer></v-spacer>
                <p class="overline font-weight-black">{{ game.location }}</p>
                <v-spacer></v-spacer>

                <p class="overline font-weight-black">{{ game.date }}</p>
              </v-card-actions>
            </v-card>
          </slide>
        </carousel-3d>
      </v-container>
      <v-divider></v-divider>
    </div>
    <v-footer dark padless rounded="">
      <v-card flat tile dark class="lighten-1 white--text text-center">
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4 white--text"
            icon
            color="primary"
            outlined
          >
            <v-icon size="24px">
              {{ icon }}
            </v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="white--text pt-0">
          Explore the world of football with our engaging content and insightful
          articles. Whether you're a die-hard fan or a casual observer, we have
          something for everyone. Stay up to date with the latest news, match
          analysis, player profiles, and in-depth features. Join our community
          of passionate football enthusiasts and share your thoughts, opinions,
          and predictions. Connect with fellow fans, participate in lively
          discussions, and celebrate the beautiful game together.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>WK</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </div>
</template>

<script>
/* eslint-disable */
import { Carousel3d, Slide } from "vue-carousel-3d";

import LandingAppBar from "@/components/LandingAppBar.vue";
export default {
  name: "LandingPage",
  components: {
    LandingAppBar,
    Carousel3d,
    Slide,
  },

  data: () => ({
    //
    loader: null,
    loading: false,
    icons: ["mdi-facebook", "mdi-twitter", "mdi-linkedin", "mdi-instagram"],
    games: [
      {
        hometeam: "Barcelona",
        awayteam: "Real Madrid",
        homescore: 0,
        awayscore: 4,
        date: "2023-04-5",
        hometeamlogo:
          "https://1000logos.net/wp-content/uploads/2016/10/Barcelona-Logo-500x313.png",
        awayteamlogo:
          "https://logos-world.net/wp-content/uploads/2020/06/Real-Madrid-Logo.png",
        stadium: "Camp Nou",
        location: "Barcelona",
      },
      {
        hometeam: "Millan",
        awayteam: "Inter Milan",
        homescore: 3,
        awayscore: 2,
        date: "2021-03-21",
        hometeamlogo:
          "https://1000logos.net/wp-content/uploads/2016/10/AC-Milan-Logo-500x281.png",
        awayteamlogo:
          "https://1000logos.net/wp-content/uploads/2021/05/Inter-Milan-logo-500x281.png",
        stadium: "San Siro",
        location: "Milan",
      },
      {
        hometeam: "Manchester United",
        awayteam: "Manchester City",
        homescore: 3,
        awayscore: 2,
        date: "2021-03-21",
        hometeamlogo:
          "https://1000logos.net/wp-content/uploads/2017/03/Manchester-United-Logo-493x500.png",
        awayteamlogo:
          "https://1000logos.net/wp-content/uploads/2017/05/Manchester-City-Logo-500x313.png",
        stadium: "Old Trafford",
        location: "Manchester",
      },
      {
        hometeam: "Liverpool",
        awayteam: "Chelsea",
        homescore: 1,
        awayscore: 1,
        date: "2021-03-21",
        hometeamlogo:
          "https://1000logos.net/wp-content/uploads/2017/04/Logo-Liverpool-500x313.png",
        awayteamlogo:
          "https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/1200px-Chelsea_FC.svg.png",
        stadium: "Anfield",
        location: "Liverpool",
      },
      {
        hometeam: "Arsenal",
        awayteam: "Tottenham",
        homescore: 3,
        awayscore: 1,
        date: "2021-03-21",
        hometeamlogo:
          "https://1000logos.net/wp-content/uploads/2016/10/Arsenal-Logo-500x313.png",
        awayteamlogo:
          "https://1000logos.net/wp-content/uploads/2018/06/Tottenham_Hotspur_Logo-640x400.png",
        stadium: "Emirates Stadium",
        location: "London",
      },
      {
        hometeam: "Bayern Munich",
        awayteam: "Borussia Dortmund",
        homescore: 4,
        awayscore: 2,
        date: "2023-04-1",
        hometeamlogo:
          "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg/2048px-FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg.png",
        awayteamlogo:
          "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/1200px-Borussia_Dortmund_logo.svg.png",
        stadium: "Allianz Arena",
        location: "Munich",
      },
      {
        hometeam: "Juventus",
        awayteam: "Inter Milan",
        homescore: 3,
        awayscore: 0,
        date: "2021-03-21",
        hometeamlogo:
          "https://upload.wikimedia.org/wikinews/en/thumb/d/d2/Juventus_Turin.svg/1255px-Juventus_Turin.svg.png",
        awayteamlogo:
          "https://1000logos.net/wp-content/uploads/2021/05/Inter-Milan-logo-500x281.png",
        stadium: "Allianz Stadium",
        location: "Turin",
      },
      {
        hometeam: "PSG",
        awayteam: " Marseille",
        homescore: 2,
        awayscore: 1,
        date: "2021-03-21",
        hometeamlogo:
          "https://1000logos.net/wp-content/uploads/2018/05/PSG-Logo-500x313.png",
        awayteamlogo:
          "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Olympique_Marseille_logo.svg/1200px-Olympique_Marseille_logo.svg.png",
        stadium: "Parc des Princes",
        location: "Paris",
      },
      {
        hometeam: "Atletico Madrid",
        awayteam: "Real Madrid",
        homescore: 1,
        awayscore: 1,
        date: "2021-03-21",
        hometeamlogo:
          "https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Atletico_Madrid_2017_logo.svg/1200px-Atletico_Madrid_2017_logo.svg.png",
        awayteamlogo:
          "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/1200px-Real_Madrid_CF.svg.png",
        stadium: "Wanda Metropolitano",
        location: "Madrid",
      },
    ],
  }),
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);
      this.loader = null;
    },
  },
};
</script>
<style scoped>
.circular-image {
  border-radius: 50%;
  width: 40px;
  height: 40px;
}
#intro_paragraph {
  font-family: "Montserrat", sans-serif;
  font-weight: 1000;
  font-size: 2rem;
}
#card_text {
  font-size: larger;
  font-weight: 1000;
}

#carusel_div {
  opacity: 0.9;
  background-color: rgba(4, 55, 77, 0.4);
}

.landingpage {
  background-image: url("https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
  opacity: 0.9;
  background-color: rgba(0, 0, 0, 0.9);
}
#overlaydiv {
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgba(4, 55, 77, 0.4);
  opacity: 0.8;
  z-index: 0.5;
}
#introtext {
  font-family: "Montserrat", sans-serif;
  font-weight: 1000;
  color: #fff;
  text-shadow: 2px 2px 4px #e97c7c;
}
#abouttext {
  font-family: "Montserrat", sans-serif;
  font-weight: 1000;
  color: #ffff;
  text-shadow: 2px 2px 4px #0000;
}
#resultstext {
  font-family: "Montserrat", sans-serif;
  font-weight: 1000;
  color: #000;
  text-shadow: 2px 2px 4px #0000;
}
#introphrase {
  font-family: "Montserrat", sans-serif;
  font-weight: 1000;
  color: #fff;
  text-shadow: 2px 2px 4px #c46b6b;
}
</style>
