<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
/* eslint-disable */

export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
<style>
#appbar {
  background-color: rgba(4, 55, 77, 0.4);
  opacity: 0.8;
  z-index: 1;
}
</style>
