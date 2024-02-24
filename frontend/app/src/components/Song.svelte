<script>
	import Upvote from './icons/Upvote.svelte';
	import Downvote from './icons/Downvote.svelte';

	export let songData, votable;
</script>

<div class="flex p-2 justify-between border border-slate-700 bg-slate-800 rounded-md mt-2">
	<div class="flex gap-4">
		<img
			src={songData}
			alt="thumb nail"
			class="w-16 aspect-square rounded-sm overflow-hidden bg-pink-300"
		/>
		<div class="flex flex-col">
			<span class="font-bold"
				><a rel="noopener noreferrer" href={songData.url}>{songData.title}</a></span
			>
			<span class="italic">by {songData.artist}</span>
		</div>
	</div>
	{#if votable}
		<div class="flex align-middle gap-4 pt-3">
			<span class="">{songData.score}</span>
			<div>
				<button><Upvote /></button>
				<button><Downvote /></button>
			</div>
		</div>
	{/if}
</div>
