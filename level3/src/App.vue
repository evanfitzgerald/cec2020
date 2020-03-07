<template>
  <div id="app">
    <p>CEC 2020 - Prorgramming</p>
      <p>
        <label for="filename">File Name: </label>
        <input id="filename" v-model="filename" :placeholder="filename">
        <button @click="getData">Load data</button>
      </p>
      <p>Rotate model: 
        <input type="checkbox" id="horizontal" v-model="horizontal">
        <label for="horizontal">Horizontal</label>
        <input type="checkbox" id="vertical" v-model="vertical">
        <label for="vertical">Vertical</label>
      </p>
    <Three ref="threecomponent" :size="size" :inputGrid="inputGrid" :vertical="vertical" :horizontal="horizontal"></Three>
  </div>
</template>

<script>
import Three from './components/Three.vue'
import axios from "axios";

export default {
  name: 'App',
  components: {
    Three
  },
  data() {
    return {
      horizontal: false,
      vertical: false,
      size: null,
      inputGrid: null,
      filename: 'easy.txt'
    }
  },
  mounted() {
    this.getData();
  },
  methods: {
    handleResponse(response) {
      this.size = response.data.size;
      this.inputGrid = response.data.grid;
      this.$refs.threecomponent.updateGrid(this.size, this.inputGrid);
    },
    handleError(error) {
      if (!error.response) {
        alert('Network error: Could not connect to server');
      } else {
        alert("'" + this.filename + "'\nFile does not exist");
      }
    },
    getData() {
      axios
        .get("http://localhost:5000/getgrid/" + this.filename)
        .then(response => (this.handleResponse(response)))
        .catch(error => (this.handleError(error)));
    }
  },
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
