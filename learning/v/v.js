document.write(12345)
const { createApp } = Vue

createApp({
  data() {
    return {
      message: 'Hello Vue!'
    }
  }
}).mount('#app')

Vue.createApp(app).mount('#app')