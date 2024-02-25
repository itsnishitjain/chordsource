<script>
	import Song from './Song.svelte';

	export let songData;
</script>

<div class="max-w-md ml-auto mr-auto">
	<div class="mb-24">
		{#each songData as song}
			<Song songData={song} votable={true} />
		{/each}
	</div>
</div>
