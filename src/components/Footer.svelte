<script>
import SizedCol from './SizedCol.svelte'
</script>

<footer class="container footer mt-5 mb-4">
    <div class="links row">
        <SizedCol id="ultimate-guide">
            <strong>
                <a href="https://gumroad.com/l/hgHhj">
                    The Ultimate Guide to Web Apps in Go
                </a>
            </strong>
        </SizedCol>
    </div>
    <div class="links row">
        <div class="offset-sm-2 col-sm-8">
            <a class="mr-2" href="https://github.com/arschles">
                github.com/arschles
                <img 
					alt="Link to my GitHub profile"
                    class="github"
                    src="/images/github.svg"
                />
            </a>◾
            <a
                class="ml-2 mr-2"
                href="https://twitter.com/arschles"
            >
                @arschles
                <img
					alt="Link to my Twitter feed"
                    class="twitter"
                    src="/images/twitter.svg"
                />
            </a>◾
            <a
                class="ml-2 mr-2"
                href="https://gifm.dev"
            >
                Go in 5 Minutes
                <img
                    style="max-height:20px"
					alt="Go in 5 Minutes Gopher"
                    class="gifm"
                    src="/images/gifm.png"
                />
            </a>◾
            <a
                class="ml-2 mr-2"
                href="/index.xml"
            >
                RSS
                <img
					alt="RSS feed"
                    class="rss"
                    src="/images/rss.svg"
                />
            </a>
        </div>
    </div>
    <div class="copyright row">
        <div class="offset-sm-2 col-sm-10">
			Copyright &copy; 2017-2020 Aaron Schlesinger
        </div>
    </div>
</footer>

<style>
footer img {
    max-width: 15px;
    display: inline;
}
a {
    color: black;
    display:inline;
}
</style>
