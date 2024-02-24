<script>
	import Song from './Song.svelte';
	import dummyData from '$lib/dummyData';

	let songsinQueue = dummyData.slice(1, 4);
</script>

<div>
	{#each songsinQueue as song}
		<Song songData={song} votable={false} />
	{/each}
</div>
