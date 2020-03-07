<template>
  <div id="container" />
</template>

<script>
import * as Three from 'three'

export default {
  name: 'Three',
  props: {
    horizontal: Boolean,
    vertical: Boolean,
    invert: Boolean,
    size: Number,
    inputGrid: Array
  },
  data() {
    return {
      camera: null,
      scene: null,
      renderer: null,
      grid: null
    }
  },
  methods: {
    init() {
      let container = document.getElementById('container');

      this.camera = new Three.PerspectiveCamera(70, container.clientWidth/container.clientHeight, 1, 1000);
      this.camera.position.z = 2 * this.$props.size;
      this.camera.position.y = 0

      this.scene = new Three.Scene();
      this.scene.background = new Three.Color( 0xf0f0f0 );
      this.updateGrid(this.$props.size, this.$props.inputGrid);

      this.renderer = new Three.WebGLRenderer({ antialias: true });
      this.renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(this.renderer.domElement);
    },
    animate() {
      requestAnimationFrame(this.animate);
      var rotation = 0.01
      if (this.$props.invert) {
        rotation = -0.01;
      }
      if (this.$props.vertical) {
        this.grid.rotation.x += rotation;
      }
      if (this.$props.horizontal) {
        this.grid.rotation.y += rotation;
      }
      this.renderer.render(this.scene, this.camera);
    },
    updateGrid(size, inputgrid) {
      this.camera.position.z = 2 * size;
      var cubesize = 1;
      var spacing = 1.1;
      this.scene.remove(this.grid);
      this.grid = new Three.Group(); // just to hold them all together
      for (var w = 0; w < size; w++) {
        for (var h=0; h < size; h++) {
          for (var d=0; d < size; d++) {
            if (inputgrid && inputgrid[w][h][d]) {
              var color = this.colorCodeFor(inputgrid[w][h][d]);
              var box = new Three.Mesh(new Three.BoxGeometry(cubesize,cubesize,cubesize),
                        new Three.MeshBasicMaterial({ color }));
              box.position.x = (h-size/2) * spacing;
              box.position.y = (w-size/2) * spacing;
              box.position.z = (d-size/2) * spacing;
              this.grid.add(box);
            }
          }
        }
      }
      this.scene.add(this.grid);
    },
    colorCodeFor(val) {
      let num = (val[0] << 16) + (val[1] << 8) + val[2];
      return num;
    }
  },
  mounted() {
    this.init();
    this.animate();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#container {
  min-height: 100%;
}
</style>
