<script>
	let songUrl = '';
	const addSong = (e) => {
		e.preventDefault();
		console.log('GET /add' + songUrl);
	};
</script>

<form
	class="fixed bottom-0 left-0 right-0 p-4 max-h-24 flex justify-center align-middle bg-base-300"
	on:submit={(e) => addSong(e)}
>
	<div class="pr-16">
		<label>
			<input
				bind:value={songUrl}
				type="url"
				name="spotify_song_url"
				id="song_url"
				placeholder="Enter a spotify link"
				class="input w-svw max-w-xs rounded-md p-2"
			/>
		</label>
	</div>
	<button class="btn btn-outline" type="submit">Add</button>
</form>
