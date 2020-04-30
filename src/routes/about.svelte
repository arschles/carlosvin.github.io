<script>
import about from './about.md'
import MainPage from "../components/MainPage.svelte"
import SizedCol from "../components/SizedCol.svelte"

let aboutHTML = about.html
</script>
<svelte:head>
	<title>About</title>
</svelte:head>

<MainPage>
  <div id="body" class="row">
    <SizedCol>
		{@html aboutHTML}
	</SizedCol>
  </div>
</MainPage>
