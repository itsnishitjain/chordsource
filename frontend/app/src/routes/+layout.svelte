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

<div class="background--custom">
	<canvas id="canvas" />
</div>

<svelte:head>
	<script async src="https://cdn.jsdelivr.net/gh/greentfrapp/pocoloco@minigl/minigl.js"></script>
</svelte:head>

<slot />

<style>
	.background--custom {
		background-color: #ffffff;
		width: 100vw;
		height: 100vh;
		position: fixed;
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
		opacity: 0.5;
	}
</style>
