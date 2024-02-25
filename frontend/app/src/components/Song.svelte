<script>
	import Upvote from './icons/Upvote.svelte';

	export let songData, votable;

	const handleUpvote = async () => {
		await fetch(`http://0.0.0.0:8080/vote?url=${songData.song.url.slice(31, 53)}`, {
			method: 'POST'
		});
	};
</script>

{#if songData.song}
	<div class="flex align-middle p-2 justify-between bg-white bg-opacity-50 rounded-md mt-2">
		<div class="flex gap-4">
			<img
				src={songData.song.image_url}
				alt="thumb nail"
				class="w-16 aspect-square rounded-sm overflow-hidden bg-pink-300"
			/>
			<div class="flex flex-col text-slate-800">
				<span class="font-bold"
					><a rel="noopener noreferrer" href={songData.song.url}>{songData.song.name}</a></span
				>
				<span class="italic">by {songData.song.artist}</span>
			</div>
		</div>
		{#if votable}
			<div class="flex items-center gap-4 text-slate-800">
				<span class="h-6">{Math.round(songData.score * 100)}</span>
				<div class="h-6">
					<button on:click={handleUpvote}><Upvote /></button>
				</div>
			</div>
		{/if}
	</div>
{/if}
