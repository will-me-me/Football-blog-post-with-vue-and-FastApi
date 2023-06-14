/* eslint-disable */

import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";

//import pinia
import { createPinia } from "pinia";
// import { PiniaPlugin } from "@pinia/vue-composition-api";

Vue.use(createPinia());

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
