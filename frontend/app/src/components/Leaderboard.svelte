<script>
	import VotableSong from './VotableSong.svelte';

	import songData from '$lib/dummyData';
</script>

<div>
	{#each songData as song}
		<VotableSong songData={song} />
	{/each}
</div>
