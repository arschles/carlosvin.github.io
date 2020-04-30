<script>
import speaking from './speaking.md'
import MainPage from '../components/MainPage.svelte'
import SizedCol from '../components/SizedCol.svelte'
let speakingHTML = speaking.html
</script>

<svelte:head>
	<title>Speaking</title>
</svelte:head>

<MainPage>
  <div id="body" class="row">
    <SizedCol>
      {@html speakingHTML}
    </SizedCol>
  </div>
</MainPage>

