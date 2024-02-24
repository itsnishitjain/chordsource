<script>
	import Form from '../../components/Form.svelte';
	import Leaderboard from '../../components/Leaderboard.svelte';
	import NowPlaying from '../../components/NowPlaying.svelte';
	import Queue from '../../components/Queue.svelte';
</script>

<header>
	<span>hacktrinity </span>
</header>

<!-- now playing -->
<section class="p-2 mb-4">
	<h1 class="font-bold text-xl">Now playing</h1>
	<NowPlaying />
</section>

<!-- up next -->
<section class="p-2 mb-4">
	<h1 class="font-bold text-xl">Up next</h1>
	<Queue />
</section>

<!-- leaderboard -->
<section class="p-2 mb-4">
	<h1 class="font-bold text-xl">Leaderboard</h1>
	<Leaderboard />
</section>

<!-- form -->
<section>
	<Form />
</section>
