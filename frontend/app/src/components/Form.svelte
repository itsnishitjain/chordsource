<script>
	let songUrl = '';
	const addSong = (e) => {
		e.preventDefault();
		console.log('GET /add' + songUrl);
	};
</script>

<form
	class="fixed bottom-0 left-0 right-0 p-4 flex justify-center align-middle bg-slate-500"
	on:submit={(e) => addSong(e)}
>
	<label>
		<input bind:value={songUrl} type="url" name="spotify_song_url" id="song_url" />
	</label>

	<button type="submit"> Add! </button>
</form>
