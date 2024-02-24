<script>
	import Song from './Song.svelte';
	import dummyData from '$lib/dummyData';

	let songsinQueue = dummyData.slice(1, 4);
</script>

<div class="max-w-md ml-auto mr-auto">
	<div>
		{#each songsinQueue as song}
			<Song songData={song} votable={false} />
		{/each}
	</div>
</div>
