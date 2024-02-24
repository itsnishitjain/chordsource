<script>
	import Song from './Song.svelte';
	import dummyData from '$lib/dummyData';
	let nowPlaying = dummyData[0];
</script>

<div class="max-w-md ml-auto mr-auto">
	<div>
		<div>
			<Song songData={nowPlaying} />
		</div>
	</div>
</div>
