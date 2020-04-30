<script>
	import NavEntry from './NavEntry.svelte';
	import SizedCol from './SizedCol.svelte';
	export let segment;
	export let siteName;

	function toggle(){
		open = !open;
	}
	let open = false;

	export let showNav = true;
</script>

<div class="container mt-2">
	{#if showNav}
	<div class="row">
		<SizedCol>
			<NavEntry
				href='/about'
				segment={segment}
			>
				about
			</NavEntry>
			<NavEntry
				href="/speaking"
				segment={segment}
			>
				speaking
			</NavEntry>
			<NavEntry
				href="/teaching"
				segment={segment}
			>
				teaching
			</NavEntry>
		</SizedCol>
	</div>
	{/if}
	<div class="row">
		<div class="offset-sm-2">
			<h1><a href="/">arschles.com</a></h1>
		</div>
	</div>
</div>
