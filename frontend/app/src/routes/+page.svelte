<!-- <h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p> -->

<script>
	import { goto } from '$app/navigation';

	let uid = '';

	const goToList = (e) => {
		e.preventDefault();

		if (uid == 'hackTrinity') {
			goto('/hackTrinity');
		}
	};
</script>

<div class="h-screen">
	<div class="hero h-full">
		<div class="hero-content flex flex-col justify-center items-center">
			<h1 class="max-w-md text-center text-5xl font-bold p-4 text-black">chordsource</h1>
			<div class="bg-white w-full max-w-md h-1/4 p-4 bg-opacity-35 rounded-md mb-8">
				<p class="py-6 text-black text-center">
					Enhance your venue's vibe with chordsource, the ultimate communal music playlist that
					unites the crowd through shared tunes, creating a dynamic and diverse musical atmosphere.
				</p>
			</div>
			<form class="max-w-md text-center" on:submit={(e) => goToList(e)}>
				<input
					id="inputbox"
					type="text"
					bind:value={uid}
					placeholder="Enter code"
					class="input w-full max-w-xs rounded-md p-3"
				/>
			</form>
		</div>
	</div>
</div>
