<script>
	import NavEntry from './NavEntry.svelte';
	export let segment;
	export let siteName;

	function toggle(){
		open = !open;
	}
	let open = false;
</script>

<style>
	nav {
		border-bottom: 1px solid rgba(255,62,0,0.1);
		font-weight: 300;
		padding: 0 1em;
		display: flex;
		justify-content: space-between;
	}

	ul {
		margin: 0;
		padding: 0;
	}

	/* clearfix */
	ul::after {
		content: '';
		display: block;
		clear: both;
	}

	button {
		display: none;
	}

	@media only screen and (max-width: 600px) {
		ul.open {
			display: flex;
			flex-flow: column;
		}

		ul.closed {
			display: none;
		}

		button {
			display: flex;
			justify-content: flex-start;
			background: transparent;
			border: none;
			font-size: 2em;
			vertical-align: top;
			height: 2em;
		}
	}

</style>

<div class="container mt-2">
	<div class="row">
		<div class="offset-sm-2">
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
		</div>
	</div>
	<div class="row">
		<div class="offset-sm-2">
			<h1><a href="/">arschles.com</a></h1>
		</div>
	</div>
</div>
