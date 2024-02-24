<script>
	import Upvote from './icons/Upvote.svelte';
	import Downvote from './icons/Downvote.svelte';

	export let songData, votable;
</script>

<div class="flex p-2 justify-between border border-slate-700">
	<div class="flex flex-col">
		<span class="font-bold"
			><a rel="noopener noreferrer" href={songData.url}>{songData.title}</a></span
		>
		<span class="italic">by {songData.artist}</span>
	</div>
	{#if votable}
		<div class="flex align-middle gap-4">
			<span class="">{songData.score}</span>
			<div>
				<button><Upvote /></button>
				<button><Downvote /></button>
			</div>
		</div>
	{/if}
</div>
