<template>
  <div id="container" />
</template>

<script>
import * as Three from 'three'

export default {
  name: 'Three',
  props: {
    horizontal: Boolean,
    vertical: Boolean
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
    init: function() {
      let container = document.getElementById('container');

      this.camera = new Three.PerspectiveCamera(70, container.clientWidth/container.clientHeight, 0.01, 10);
      this.camera.position.z = 10
      this.camera.position.y = 0

      this.scene = new Three.Scene();
      // this.scene.background = new Three.Color( 0xf0f0f0 );

      var n = 3;
      var size = 1;
      var spacing = 1.1;
      this.grid = new Three.Group(); // just to hold them all together
      for (var w = 0; w < n; w++) {
        for (var h=0; h < n; h++) {
          for (var d=0; d < n; d++) {
            var box = new Three.Mesh(new Three.BoxGeometry(size,size,size),
                          new Three.MeshBasicMaterial({ color: Math.random() * 0xffffff }));
            box.position.x = (h-n/2) * spacing;
            box.position.y = (w-n/2) * spacing;
            box.position.z = (d-n/2) * spacing;
            this.grid.add(box);
          }
        }
      }
      this.scene.add(this.grid);

      this.renderer = new Three.WebGLRenderer({ antialias: true });
      this.renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(this.renderer.domElement);
    },
    animate: function() {
      requestAnimationFrame(this.animate);
      if (this.$props.vertical) {
        this.grid.rotation.x += 0.01;
      }
      if (this.$props.horizontal) {
        this.grid.rotation.y += 0.01;
      }
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
#container {
  min-height: 100%;
}
</style>
