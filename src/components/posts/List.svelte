
<script>
import Entry from './Entry.svelte';
import SizedCol from "../SizedCol.svelte";
export let posts;
</script>


{#each posts as post}
  <div class="post mb-2" id={post.slug}>
    <Entry {post}/>
  </div>
{/each}

