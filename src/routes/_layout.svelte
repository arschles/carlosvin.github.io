<script>
	import Nav from '../components/Nav.svelte';
	import Footer from '../components/Footer.svelte'
  	import { getSiteName } from "../services/lang";
	import Social from '../components/Social.svelte';
	import IconLink from '../components/IconLink.svelte';

	export let segment;

	const siteName = getSiteName();
	const rssTitle = `Subscribe to ${siteName}`;
	const rssUrl = `/rss`;
</script>

<svelte:head>
	<link
		rel="alternate"
		type="application/rss+xml"
		title={rssTitle}
		href={rssUrl} />
</svelte:head>

<main class="mt-2" segment={segment}>
	<slot></slot>
</main>

<Footer/>