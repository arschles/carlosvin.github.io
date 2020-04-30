
<script>
    function curr(segment, href) {
        if (segment === undefined && href === '.') {
            return 'page';
        } else if (href.startsWith(segment)) {
            return 'page';
        } else {
            return undefined;
        }
    }

    export let segment;
    export let href;


    $: current = curr(segment, href);
</script>

<style>
	a {
		text-decoration: none;
		padding: 1em 0.5em;
	}
</style>

<a
	type="button"
	class="btn btn-link text-dark"
	href={href}
>
	<slot></slot>
</a>
