<script>
	import genreData from '$lib/dummyMood';
	import Chart from 'chart.js/auto';
	import { onMount } from 'svelte';

	onMount(async function () {
		new Chart(document.getElementById('genre-chart'), {
			type: 'doughnut',
			data: {
				labels: genreData.map((row) => row.genre),
				datasets: [
					{
						label: 'Listens',
						data: genreData.map((row) => row.listens)
					}
				]
			}
		});
	});
</script>

<div class="bg-white bg-opacity-50 p-4 rounded-md">
	<canvas id="genre-chart"></canvas>
</div>
