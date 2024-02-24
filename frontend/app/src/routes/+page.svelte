<!-- <h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p> -->

<script>
	const backgroundGradient = () => {
		var gradient = new Gradient();
		gradient.initGradient('#canvas');
	};

	import { goto } from '$app/navigation';
	let uid = '';

	const goToList = (e) => {
		e.preventDefault();

		if (uid == 'hackTrinity') {
			goto('/hackTrinity');
		}
	};
</script>

<svelte:head>
	<script
		async
		src="https://cdn.jsdelivr.net/gh/greentfrapp/pocoloco@minigl/minigl.js"
		on:load={() => backgroundGradient()}
	></script>
</svelte:head>

<slot />

<div class="background--custom">
	<canvas id="canvas" />
</div>

<div class="hero min-h-screen bg-base-200">
	<div class="hero-content flex h-screen justify-center items-center">
		<h1 class="max-w-md text-center text-5xl font-bold p-8 text-white">Group 10</h1>
		<form class="max-w-md text-center" on:submit={(e) => goToList(e)}>
			<input
				id="inputbox"
				type="text"
				bind:value={uid}
				placeholder="Enter code"
				class="input input-bordered w-full max-w-xs rounded-md p-3"
			/>
		</form>
	</div>
</div>

<style>
	.background--custom {
		background-color: #ffffff;
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
