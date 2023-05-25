<template>
  <div class="landingpage">
    <landing-app-bar />
    <div id="overlaydiv" class="rounded-lg">
      <h1 class="display-1 text-center" id="introtext">Simple Rules</h1>
      <h2 class="display-4 text-center" id="introphrase">
        Take The Ball Pass the Ball
      </h2>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

import LandingAppBar from "@/components/LandingAppBar.vue";
export default {
  name: "LandingPage",
  components: {
    LandingAppBar,
  },

  data: () => ({
    //
    games: [
      {
        hometeam: "Barcelona",
        awayteam: "Real Madrid",
        homescore: 3,
        awayscore: 2,
        date: "2021-03-21",
      },
      {
        hometeam: "Millan",
        awayteam: "Juventus",
        homescore: 3,
        awayscore: 2,
        date: "2021-03-21",
      },
      {
        hometeam: "Manchester United",
        awayteam: "Manchester City",
        homescore: 3,
        awayscore: 2,
        date: "2021-03-21",
      },
    ],
  }),
};
</script>
<style>
.landingpage {
  background-image: url("https://images.unsplash.com/photo-1556816213-00d1ffaa2f78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
  opacity: 0.8;
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
  border: 2px solid #131212;
}
#introtext {
  font-family: "Montserrat", sans-serif;
  font-weight: 1000;
  color: #fff;
  text-shadow: 2px 2px 4px #e97c7c;
}
#introphrase {
  font-family: "Montserrat", sans-serif;
  font-weight: 1000;
  color: #fff;
  text-shadow: 2px 2px 4px #c46b6b;
}
</style>
