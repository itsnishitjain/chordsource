<script>
	import Form from '../../components/Form.svelte';
	import Chart from '../../components/icons/Chart.svelte';
	import Leaderboard from '../../components/Leaderboard.svelte';
	import NowPlaying from '../../components/NowPlaying.svelte';
	import { onMount } from 'svelte';

	export let data;

	let queue = data.res.queue;
	queue.sort((a, b) => b.score - a.score);

	let nowPlaying = data.res.history.sort((a, b) => b.timestamp - a.timestamp)[0];

	onMount(() => {
		setInterval(async () => {
			let res = await fetch('http://0.0.0.0:8080/status', {
				method: 'GET'
			});

			res = await res.json();
			let resQueue = res.queue;
			let resHist = await res.history;

			queue = resQueue.sort((a, b) => {
				b.score - a.score;
			});

			nowPlaying = resHist.sort((a, b) => b.timestamp - a.timestamp)[0];
		}, 15000);
	});
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
		<NowPlaying songData={nowPlaying} />
	</div>
</section>

<!-- leaderboard -->
<section class="p-2 mb-4">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6 text-base-300">Leaderboard</h1>
		<Leaderboard songData={queue} />
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
