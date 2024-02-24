<script>
	import Song from './Song.svelte';

	import dummyData from '$lib/dummyData';

	let songData = dummyData.slice(4);
</script>

<div class="max-w-md ml-auto mr-auto">
	<div class="mb-16">
		{#each songData as song}
			<Song songData={song} votable={true} />
		{/each}
	</div>
</div>
