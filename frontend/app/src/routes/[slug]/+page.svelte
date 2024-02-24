<script src="https://kit.fontawesome.com/41288383b3.js" crossorigin="anonymous">
	import Form from '../../components/Form.svelte';
	import Leaderboard from '../../components/Leaderboard.svelte';
	import NowPlaying from '../../components/NowPlaying.svelte';
	import Queue from '../../components/Queue.svelte';
</script>

<header>
	<div class="navbar bg-base-300">
		<div class="flex-1">
			<a class="btn btn-ghost text-xl">Group10</a>
		</div>
		<div class="flex-none">
			<div class="dropdown dropdown-end">
				<div tabindex="0" role="button" class="btn btn-ghost btn-circle">
					<div class="indicator">
						<i class="fa-solid fa-chart-simple"></i>
					</div>
				</div>
				<div
					tabindex="0"
					class="mt-3 z-[1] card card-compact dropdown-content w-52 bg-base-100 shadow"
				>
					<div class="card-body">
						<span class="font-bold text-lg">8 Items</span>
						<span class="text-info">Subtotal: $999</span>
						<div class="card-actions">
							<button class="btn btn-primary btn-block">View cart</button>
						</div>
					</div>
				</div>
			</div>
			<div class="dropdown dropdown-end">
				<div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
					<div>
						<i class="fa-solid fa-music"></i>
					</div>
				</div>
				<ul
					tabindex="0"
					class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
				>
					<li>
						<a class="justify-between">
							Profile
							<span class="badge">New</span>
						</a>
					</li>
					<li><a>Settings</a></li>
					<li><a>Logout</a></li>
				</ul>
			</div>
		</div>
	</div>
</header>

<!-- now playing -->
<section class="p-2 mb-4 pt-8">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6">Now playing</h1>
		<NowPlaying />
	</div>
</section>

<!-- up next -->
<section class="p-2 mb-4">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6">Up next</h1>
		<Queue />
	</div>
</section>

<!-- leaderboard -->
<section class="p-2 mb-4">
	<div class="max-w-md ml-auto mr-auto">
		<h1 class="font-bold text-xl pb-6">Leaderboard</h1>
		<Leaderboard />
	</div>
</section>

<!-- form -->
<section>
	<Form />
</section>
