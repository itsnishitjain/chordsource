<style>
  .background--custom {
    background-color: #FFFFFF;
    width: 100vw;
    height: 100vh;
    position: absolute;
    overflow: hidden;
    z-index: -2;
    top: 0;
    left: 0;
  }
  canvas#canvas {
    z-index: -1;
    position: absolute;
    width: 100%;
    height: 100%;
    transform: rotate(-12deg) scale(2) translateY(0%);
    --gradient-color-1: #ef008f; 
    --gradient-color-2: #6ec3f4; 
    --gradient-color-3: #7038ff;  
    --gradient-color-4: #ffba27;
    --gradient-speed: 0.000006;
  }
</style>

<script>
  import "../app.css"

  const backgroundGradient = () => {
    var gradient = new Gradient();
    gradient.initGradient("#canvas");
  }
</script>


<div class="background--custom">
  <canvas id="canvas" />
  <slot />
  
</div>

<svelte:head>
  <script async src="https://cdn.jsdelivr.net/gh/greentfrapp/pocoloco@minigl/minigl.js" on:load={() => backgroundGradient()}/>
</svelte:head>

