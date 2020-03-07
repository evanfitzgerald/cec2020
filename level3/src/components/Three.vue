<template>
  <div id="container" />
</template>

<script>
import * as Three from 'three'

export default {
  name: 'Three',
  data() {
    return {
      camera: null,
      scene: null,
      renderer: null,
      cube: null
    }
  },
  methods: {
    init: function() {
      let container = document.getElementById('container');

      this.camera = new Three.PerspectiveCamera(70, 1, 0.01, 10);
      this.camera.position.z = 5;

      this.scene = new Three.Scene();

      const geometry = new Three.BoxGeometry(1, 1, 1)
      const material = new Three.MeshBasicMaterial({ color: 0x00ff00 })
      this.cube = new Three.Mesh(geometry, material)
      this.scene.add(this.cube)

      this.renderer = new Three.WebGLRenderer();
      console.log('Height, width:', container.clientWidth, container.clientHeight);
      this.renderer.setSize(800, 800);
      container.appendChild(this.renderer.domElement);
    },
    animate: function() {
      requestAnimationFrame(this.animate);
      this.cube.rotation.x += 0.01;
      this.cube.rotation.y += 0.02;
      this.renderer.render(this.scene, this.camera);
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
</style>
