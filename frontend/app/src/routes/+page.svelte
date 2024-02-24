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

<slot />

<div class="hero min-h-screen">
	<div class="hero-content flex flex-col h-screen justify-center items-center">
		<h1 class="max-w-md text-center text-5xl font-bold p-8 text-black">Group 10</h1>
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
