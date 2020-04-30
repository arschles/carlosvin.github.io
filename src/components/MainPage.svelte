<script context="module">
  import Nav from "../components/Nav.svelte"
  import SizedCol from "../components/SizedCol.svelte"
  import { getSiteName, getDescription } from "../services/lang";
</script>


<svelte:head>
  <title>{getSiteName()}</title>
  <meta name="description" content={getDescription()} />
</svelte:head>

<div class="container">
  <div id="nav-container" class="row">
    <SizedCol>
      <Nav></Nav>
    </SizedCol>
  </div>
  <slot></slot>
</div>

<style>
#nav-container {
  margin-bottom:2em;
}
</style>