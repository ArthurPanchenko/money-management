import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookie from "vue3-cookies"

createApp(App).use(router).use(VueCookie).mount('#app')

export const axiosUrl = 'http://127.0.0.1:8000'
