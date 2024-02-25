<script>
	import Song from './Song.svelte';

	export let songData;
</script>

<div class="max-w-md ml-auto mr-auto">
	<div>
		<div>
			<Song {songData} />
		</div>
	</div>
</div>
