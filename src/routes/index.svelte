<script context="module">
  export async function preload({ params, query }) {
    this.fetch(`rss`);
    this.fetch('sitemap.xml');
    return this.fetch(`index.json`)
      .then(r => r.json())
      .then(posts => {
        return { posts };
      });
  }
</script>

<script>
  import MainPage from "../components/MainPage.svelte"
  import List from "../components/posts/List.svelte";
  import Nav from "../components/Nav.svelte"
  import index from './index.md'
  import SizedCol from "../components/SizedCol.svelte"
  import { getSiteName, getDescription } from "../services/lang";

  export let posts;
  $: numPosts = posts ? posts.length : 0;
</script>

<svelte:head>
  <title>{getSiteName()}</title>
  <meta name="description" content={getDescription()} />
</svelte:head>

<MainPage>
    <div id="body" class="row">
    <SizedCol>
      {@html index.html}
    </SizedCol>
  </div>
  <hr />
  <div id="posts-list" class="row">
    <SizedCol>
      <List posts={posts} />
    </SizedCol>
  </div>
</MainPage>

<style>
  div#body{
    font-family: "Lucida Console", "Monaco", "monospace";
    font-size: 1.2em;
  }
</style>

