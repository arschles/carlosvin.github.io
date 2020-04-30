
<script>
import Entry from './Entry.svelte';
import SizedCol from "../SizedCol.svelte";
export let posts;
</script>


<div class="container content posts-list">
  {#each posts as post}
  <div class="row">
    <SizedCol>
      <Entry {post}/>
    </SizedCol>
  </div>
  {/each}
</div>
