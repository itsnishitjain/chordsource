<script>
	import Song from './Song.svelte';
	import dummyData from '$lib/dummyData';
	let nowPlaying = dummyData[0];
</script>

<div>
	<Song songData={nowPlaying} />
</div>
