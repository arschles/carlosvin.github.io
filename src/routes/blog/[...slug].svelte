<script context="module">
  import { path } from "../../services/models";

  export async function preload({ params, query }) {
    const [slug, lang] = params.slug;
    const res = await this.fetch(path(slug, lang) + ".json");
    const data = await res.json();

    if (res.status === 200) {
      return { post: data };
    } else if (res.status === 301) {
      return { post: data, isCanonical: true };
    } else {
      this.error(res.status, data.message);
    }
  }
  // TODO add canonical link to translations
</script>

<script>
  import { onMount } from "svelte";
  import { url } from "../../services/models";
  import { getIsoDateStr } from "../../services/dates";
  import Share from "../../components/Share.svelte";
  import MainPage from '../../components/MainPage.svelte';
  import SizedCol from '../../components/SizedCol.svelte'

  // TODO remove workaround for this issue https://github.com/sveltejs/sapper/issues/904
  onMount(async () => {
    [...document.querySelectorAll('a[href^="#"]')].map(
      x => (x.href = document.location + new URL(x.href).hash)
    );
  });

  export let post;
  export let isCanonical = false;
</script>

<style>
  
  h2 {
    font-size: 3em;
    font-family: 'Ubuntu Mono';
    margin-bottom:2px;
  }
  .date {
    font-size: 0.8em;
    font-family: 'Ubuntu Mono';
  }
  .content {
    font-size: 0.9em;
    font-family: 'Raleway';
  }

</style>

<svelte:head>
  <title>{post.title}</title>
  <meta name="date" content={getIsoDateStr(post.date)} scheme="YYYY-MM-DD" />
  <meta name="description" content={post.summary} />
  {#if isCanonical}
    <link rel="canonical" href={path(post.slug, post.lang)} />
  {/if}
  <link
    rel="preload"
    href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/vs.min.css"
    as="style"
    onload="this.onload=null;this.rel='stylesheet'" />
  <noscript>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/vs.min.css" />
  </noscript>
</svelte:head>

<MainPage>
  <div id="body" class="row">
    <SizedCol>
      <header>
        <h2>
          {post.title}
        </h2>
        <p class="date">{post.date} </p>
      </header>

      <div class="content">
        {@html post.html}
      </div>
    </SizedCol>
  </div>
</MainPage>

