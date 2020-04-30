<script>
import about from './about.md'
let aboutHTML = about.html
</script>
<svelte:head>
	<title>About</title>
</svelte:head>

{@html aboutHTML}
