<script>
	let songUrl = '';
	const addSong = async (e) => {
		e.preventDefault();

		let res = await fetch(`http://0.0.0.0:8080/vote?url=${songUrl.slice(31, 53)}`, {
			method: 'POST'
		});

		console.log(res);
	};
</script>

<form
	class="fixed bottom-0 left-0 right-0 p-4 gap-4 justify-center max-h-24 flex bg-base-300"
	on:submit={(e) => addSong(e)}
>
	<input
		bind:value={songUrl}
		type="url"
		name="spotify_song_url"
		id="song_url"
		placeholder="Enter a spotify link"
		class="input w-svw max-w-xs shrink rounded-md p-2"
	/>
	<button class="btn btn-outline flex" type="submit">Add</button>
</form>
