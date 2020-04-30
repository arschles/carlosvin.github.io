<script>
	import NavEntry from './NavEntry.svelte';
	import SizedCol from './SizedCol.svelte';

	export let segment;
</script>

<div id="nav-links">
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
<h1 id="name-header">
  <a href="/">arschles.com</a>
</h1>
