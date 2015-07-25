# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

BLOG_AUTHOR = u"Carlos Martín Sánchez"
BLOG_TITLE = u"Vin's Blog"
SITE_URL = "http://carlosvin.github.io/"
# BASE_URL = "http://getnikola.com/"
BLOG_EMAIL = "carlosvin@gmail.com"
BLOG_DESCRIPTION = "Web personal de Carlos Martín Sánchez: Cuento lo que pasa por la web o por mi cabeza."

WRITE_TAG_CLOUD = True

# What is the default language?
DEFAULT_LANG = "es"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    "en": "./en",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.rst.pl will be considered
# its Polish translation.
#     (in the above example: path == "something", lang == "pl", ext == "rst")
# this pattern is also used for metadata:
#     something.meta -> something.meta.pl

TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"

# If you don't want your Polish files to be considered Perl code, use this:
# TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"
#     Note that this pattern will become the default in v7.0.0.

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/archive.html', u'Archivos'),
        ('/categories/index.html', u'Categorías'),
        ('/rss.xml', 'RSS'),
        ('https://cse.google.com/cse/publicurl?cx=016672377533739393798:3kwbrrevcdc', 'Buscar'),
    ),
    'en': (
        ('/en/archive.html', 'Archives'),
        ('/en/categories/index.html', 'Tags'),
        ('/en/rss.xml', 'RSS'),
        ('https://cse.google.com/cse/publicurl?cx=016672377533739393798:3kwbrrevcdc', 'Search'),
    ),
}

# Below this point, everything is optional

# While nikola can select a sensible locale for each language,
# sometimes explicit control can come handy.
# In this file we express locales in the string form that
# python's locales will accept in your OS, by example
# "en_US.utf8" in unix-like OS, "English_United States" in Windows.
# LOCALES = dict mapping language --> explicit locale for the languages
# in TRANSLATIONS. You can ommit one or more keys.
# LOCALE_FALLBACK = locale to use when an explicit locale is unavailable
# LOCALE_DEFAULT = locale to use for languages not mentioned in LOCALES; if
# not set the default Nikola mapping is used.

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
("posts/*.rst", "posts", "post.tmpl"),
("posts/*.txt", "posts", "post.tmpl"),
)
PAGES = (
("stories/*.rst", "stories", "story.tmpl"),
("stories/*.txt", "stories", "story.tmpl"),
)

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
"rest": ('.rst', '.txt'),
"markdown": ('.md', '.mdown', '.markdown'),
"textile": ('.textile',),
"txt2tags": ('.t2t',),
"bbcode": ('.bb',),
"wiki": ('.wiki',),
"ipynb": ('.ipynb',),
"html": ('.html', '.htm'),
# PHP files are rendered the usual way (i.e. with the full templates).
# The resulting files have .php extensions, making it possible to run
# them without reconfiguring your server to recognize them.
"php": ('.php',),
# Pandoc detects the input from the source filename
# but is disabled by default as it would conflict
# with many of the others.
# "pandoc": ('.rst', '.md', '.txt'),
}

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# HIDE_UNTRANSLATED_POSTS = False

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
# REDIRECTIONS = []

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola install_plugin ping`).
# To do manual deployment, set it to []
# DEPLOY_COMMANDS = []

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.
#
# Many filters are shipped with Nikola.  A list is available in the manual:
# <http://getnikola.com/handbook.html#post-processing-filters>
# FILTERS = {
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
# GALLERY_PATH = "galleries"
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to 'old posts, page %d' or 'page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
# INDEXES_TITLE = ""         # If this is empty, defaults to BLOG_TITLE
# INDEXES_PAGES = ""         # If this is empty, defaults to '[old posts,] page %d' (see above)
# INDEXES_PAGES_MAIN = False # If True, INDEXES_PAGES is also displayed on
                             # the main (the newest) index page (index.html)

# Name of the theme to use.
THEME = "def"


# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# date format used to display post dates.
# (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'
DATE_FORMAT = '%Y-%m-%d'

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# For creating favicons, take a look at:
# http://www.netmagazine.com/features/create-perfect-favicon
# FAVICONS = {
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# }

# Show only teasers in the index pages? Defaults to False.
INDEX_TEASERS = True

# A HTML fragment with the Read more... link.
# The following tags exist and are replaced for you:
# {link}        A link to the full post page.
# {read_more}   The string “Read more” in the current language.
# {{            A literal { (U+007B LEFT CURLY BRACKET)
# }}            A literal } (U+007D RIGHT CURLY BRACKET)
# READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'

# A HTML fragment describing the license, for the sidebar.
#LICENSE = ""
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
LICENSE = """
   <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
   <img alt="Creative Commons License BY-NC-SA"
   style="border-width:0; margin-bottom:12px;"
   src="http://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="http://getnikola.com" rel="nofollow">Nikola</a>         {license}'
CONTENT_FOOTER = CONTENT_FOOTER.format(email=BLOG_EMAIL,
                                       author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year,
                                       license=LICENSE)

# To use comments, you can choose between different third party comment
# systems, one of "disqus", "livefyre", "intensedebate", "moot",
#                 "googleplus", "facebook" or "isso"
COMMENT_SYSTEM = "googleplus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "carlosvin@gmail.com"

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
# STRIP_INDEXES = False

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
PRETTY_URLS = T

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False
# If True, schedules post to today if possible, even if scheduled hour is over
# SCHEDULE_FORCE_TODAY = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
#MATHJAX_CONFIG = """
#<script type="text/x-mathjax-config">
#MathJax.Hub.Config({
#    tex2jax: {
#        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#    },
#    displayAlign: 'left', // Change this to 'center' to center equations.
#    "HTML-CSS": {
#        styles: {'.MathJax_Display': {"margin": 0}}
#    }
#});
#</script>
#"""

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuracion you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What MarkDown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Hide link to source for the posts?
# HIDE_SOURCELINK = False
# Copy the source files for your pages?
# Setting it to False implies HIDE_SOURCELINK = True
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
RSS_TEASERS = True

# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """"""

# EXTRA_HEAD_DATA = """"""

BODY_END = """<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-1328360-9', 'carlosvin.github.io');
  ga('send', 'pageview');

</script>

<!-- Start of StatCounter Code for Default Guide -->
<script type="text/javascript">
var sc_project=9708205; 
var sc_invisible=1; 
var sc_security="4998d447"; 
var scJsHost = (("https:" == document.location.protocol) ?
"https://secure." : "http://www.");
document.write("<sc"+"ript type='text/javascript' src='" +
scJsHost+
"statcounter.com/counter/counter.js'></"+"script>");
</script>
<noscript><div class="statcounter"><a title="web analytics"
href="http://statcounter.com/" target="_blank"><img
class="statcounter"
src="http://c.statcounter.com/9708205/0/4998d447/1/"
alt="web analytics"></a></div></noscript>
<!-- End of StatCounter Code for Default Guide -->
"""


# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# Additional metadata that is added to a post when creating a new_post
#ADDITIONAL_METADATA = { 
#    'author': 'Carlos Martín Sánchez',
#}

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }


# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (eg. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use W3C-DTF Format (ex. 2012-03-30T23:00:00+02:00)
#
TIMEZONE = 'Europe/Madrid'

# If webassets is installed, bundle JS and CSS to make site loading faster
USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# Experimental plugins - use at your own risk.
# They probably need some manual adjustments - please see their respective
# readme.
# ENABLED_EXTRAS = [
#     'planetoid',
#     'ipynb',
#     'local_search',
#     'render_mustache',
# ]

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# You can configure the logging handlers installed as plugins or change the
# log level of the default stdout handler.
LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'WARNING', 'bubble': True},
    #'smtp': {
    #    'from_addr': 'test-errors@example.com',
    #    'recipients': ('test@example.com'),
    #    'credentials':('testusername', 'password'),
    #    'server_addr': ('127.0.0.1', 25),
    #    'secure': (),
    #    'level': 'DEBUG',
    #    'bubble': True
    #}
}

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# List XML-RPC services (recommended) in PING_XMLRPC_SERVICES and HTTP
# GET services (web pages) in PING_GET_SERVICES.
# Entries pointing to domains, such as Ping-o-Matic, must end with
# a forward slash to avoid having "/RPC2" appended automatically.
# Consider adding `nikola ping` as the last entry in DEPLOY_COMMANDS.
PING_XMLRPC_SERVICES = [
   "http://blogsearch.google.com/ping/RPC2",
   "http://ping.blogs.yandex.ru/RPC2",
   "http://ping.baidu.com/ping/RPC2",
   "http://rpc.pingomatic.com/",
]

PING_GET_SERVICES = [
   "http://www.bing.com/webmaster/ping.aspx?sitemap={0}".format(SITE_URL+'sitemap.xml'),
   "http://www.google.com/webmasters/tools/ping?sitemap={0}".format(SITE_URL+'sitemap.xml'),
]
