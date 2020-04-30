<script>
  import { path } from "../../services/models";
  import Entry from "../Entry.svelte";
  export let post;
</script>

<style>
  .summary {
    color: #676767;
  }
  .lang {
    padding-right: 0.2em;
    padding-left: 0.2em;
    color: #333;
  }
  .lang:not(:last-child)::after {
    content: ", ";
  }
  .description {
    display: flex;
  }

  .description > .content {
    flex-grow: 1;
    width: 0;
  }

  .subtitle {
    font-size: small;
    font-family: 'Courier New', Courier, monospace;
  }

  .date::after {
    content: " - ";
  }

  .title {
    font-size: 1.2em;
  }
</style>

<a
  rel="prefetch"
  href={path(post.slug)}
  class="title"
>
  <span class="post-title">{post.title}</span>
</a>
<span class="post-date">
  {new Date(post.date).toLocaleDateString()}
</span>
