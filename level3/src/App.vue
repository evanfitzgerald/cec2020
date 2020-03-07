<template>
  <div id="app">
    <p>CEC 2020 - Prorgramming</p>
    <span>
      <p>Rotate model</p>
      <input type="checkbox" id="horizontal" v-model="horizontal">
      <label for="horizontal">Horizontal</label>
      <input type="checkbox" id="vertical" v-model="vertical">
      <label for="vertical">Vertical</label>
    </span>
    <Three :vertical="vertical" :horizontal="horizontal"/>
  </div>
</template>

<script>
import Three from './components/Three.vue'

export default {
  name: 'App',
  components: {
    Three
  },
  data() {
    return {
      horizontal: false,
      vertical: false
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: fixed;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
}
</style>
