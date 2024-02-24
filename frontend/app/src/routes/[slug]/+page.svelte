<script>
	import Form from '../../components/Form.svelte';
	import Chart from '../../components/icons/Chart.svelte';
	import Leaderboard from '../../components/Leaderboard.svelte';
	import NowPlaying from '../../components/NowPlaying.svelte';
	import Queue from '../../components/Queue.svelte';

	export let data;
</script>

<header>
	<div class="navbar bg-base-300">
		<div class="flex-1">
			<a href="/" class="btn btn-ghost text-xl">chordsource</a>
		</div>
		<div class="flex-none">
			<div tabindex="0" role="button" class="btn btn-ghost btn-circle">
				<div class="indicator">
					<a href={'/' + data.slug + '/analytics'}><Chart /></a>
				</div>
			</div>
		</div>
	</div>
</header>

<!-- now playing -->
<section class="p-2 mb-4 pt-8">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6 text-base-300">Now playing</h1>
		<NowPlaying />
	</div>
</section>

<!-- up next -->
<section class="p-2 mb-4">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6 text-base-300">Up next</h1>
		<Queue />
	</div>
</section>

<!-- leaderboard -->
<section class="p-2 mb-4">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6 text-base-300">Leaderboard</h1>
		<Leaderboard />
	</div>
</section>

<!-- form -->
<section>
	<Form />
</section>

<!-- <style>
	.gradient {
		background: rgb(238, 174, 202);
		background: linear-gradient(
			180deg,
			rgba(238, 174, 202, 1) 0%,
			rgba(148, 187, 233, 1) 52%,
			rgba(148, 187, 233, 0) 100%
		);
	}
</style> -->
