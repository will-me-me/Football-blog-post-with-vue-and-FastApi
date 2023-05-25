/* eslint-disable */

import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
// import SplitCarousel from "vue-split-carousel";
// import "vue-split-carousel/dist/vue-split-carousel.css";

// Vue.use(SplitCarousel);

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
