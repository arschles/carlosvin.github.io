<script>
export let cols = 8
export let offset = 2
export let id
</script>

<div
    class="offset-sm-{offset} col-sm-{cols}"
    id="{id}"
>
    <slot></slot>
</div>
