<script>
  import { path } from "../../services/models";
  import Entry from "../Entry.svelte";
  export let post;
</script>

<a
  rel="prefetch"
  href={path(post.slug)}
  class="title"
>
  <span class="post-title">{post.title}</span>
</a>
<span class="post-date">
  <small>
    [{new Date(post.date).toLocaleDateString()}]
  </small>
</span>

<style>
  
  span.post-date {
    font-size: 0.8em;
    color: grey;
  }
  span.post-title {
    font-size: 1.2em;
    color: black;
  }

</style>
