<script>
	import '../app.css';
	import { onMount } from 'svelte';

	const backgroundGradient = () => {
		let gradient = new Gradient();
		gradient.initGradient('#canvas');
	};

	onMount(() => {
		backgroundGradient();
	});
</script>

<svelte:head>
	<script async src="https://cdn.jsdelivr.net/gh/greentfrapp/pocoloco@minigl/minigl.js"></script>
</svelte:head>

<div class="">
	<div class="white"></div>
	<canvas id="canvas" />
	<slot />
</div>

<style>
	.white {
		width: 100%;
		height: 100%;
		position: fixed;
		top: 0;
		left: 0;
		z-index: -2;
		background: white;
	}
	canvas#canvas {
		z-index: -1;
		position: fixed;
		top: 0;
		left: 0;
		width: 100vw;
		height: 100vh;
		transform: rotate(-12deg) scale(2) translateY(0%);
		--gradient-color-1: #ef008f;
		--gradient-color-2: #6ec3f4;
		--gradient-color-3: #7038ff;
		--gradient-color-4: #ffba27;
		--gradient-speed: 0.000006;
		opacity: 0.5;
	}
</style>
