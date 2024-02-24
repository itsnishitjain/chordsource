<script>
	import Upvote from './icons/Upvote.svelte';
	import Downvote from './icons/Downvote.svelte';

	export let songData, votable;
</script>

<div class="flex align-middle p-2 justify-between bg-white bg-opacity-50 rounded-md mt-2">
	<div class="flex gap-4">
		<img
			src={songData}
			alt="thumb nail"
			class="w-16 aspect-square rounded-sm overflow-hidden bg-pink-300"
		/>
		<div class="flex flex-col text-slate-800">
			<span class="font-bold"
				><a rel="noopener noreferrer" href={songData.url}>{songData.title}</a></span
			>
			<span class="italic">by {songData.artist}</span>
		</div>
	</div>
	{#if votable}
		<div class="flex items-center gap-4 text-slate-800">
			<span class="h-6">{songData.score}</span>
			<div class="h-6">
				<button><Upvote /></button>
				<button><Downvote /></button>
			</div>
		</div>
	{/if}
</div>
