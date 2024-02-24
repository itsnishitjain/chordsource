<script>
	import Music from '../../../components/icons/Music.svelte';
	import History from '../../../components/History.svelte';
	import Pie from '../../../components/Pie.svelte';

	export let data;
</script>

<header>
	<div class="navbar bg-base-300">
		<div class="flex-1">
			<a href="/" class="btn btn-ghost text-xl">chordsource</a>
		</div>
		<div class="flex-none">
			<div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
				<div>
					<a href={'/' + data.slug}><Music /></a>
				</div>
			</div>
		</div>
	</div>
</header>

<body class="bg-gradient-to-b from-pink-300 to-cyan-500">
	<div class="bg-gradient-to-t from-cyan-500 to-blue-500"></div>
</body>

<!-- now playing -->
<section class="p-2 mb-4 pt-8">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6 text-base-300">Current Mood</h1>
	</div>
</section>

<!-- up next -->
<section class="p-2 mb-4">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6 text-base-300">Today's Vibe</h1>
		<Pie />
	</div>
</section>

<!-- leaderboard -->
<section class="p-2 mb-4">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6 text-base-300">History</h1>
		<History />
	</div>
</section>
