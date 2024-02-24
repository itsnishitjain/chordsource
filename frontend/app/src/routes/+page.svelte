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
	<div class="hero h-3/4">
		<div class="hero-content flex flex-col justify-center items-center">
			<h1 class="max-w-md text-center text-5xl font-bold p-4 text-black">chordsource</h1>
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

	<div class="bg-white w-full h-1/4 p-4">
		<p class="py-6 text-black text-center bg-white">
			Elevate your music experience at our cafe with CrowdSourceGroove, the ultimate communal
			Spotify playlist that brings the crowd together through shared tunes! Immerse yourself in a
			dynamic musical atmosphere where every patron becomes a DJ, contributing to a collective
			playlist that reflects the diverse tastes of our vibrant community.
		</p>
	</div>
</div>
