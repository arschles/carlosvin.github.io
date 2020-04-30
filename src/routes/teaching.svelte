<script>
import teaching from './teaching.md'
import MainPage from '../components/MainPage.svelte'
import SizedCol from '../components/SizedCol.svelte'

let teachingHTML = teaching.html
</script>

<svelte:head>
	<title>Speaking</title>
</svelte:head>

<MainPage>
	<div id="body" class="row">
    <SizedCol>
      {@html teachingHTML}
		</SizedCol>
	</div>
</MainPage>