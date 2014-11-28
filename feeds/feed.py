# Importing the syndication feed and my Article class from my blog model.
from django.contrib.syndication.views import Feed
from blog.models import Article

class BlogFeed(Feed):
    # Here I am setting the default RSS information that gets shown at the top of the feed.
    title = "zrealtycorp.com"
    link = "/blog/"
    description = "Recent Blog Entries on ZachRohde.com"

    # These are my "hard-coded" author information.
    author_email = 'zach@zachrohde.com'
    author_link = 'http://zachrohde.com'

    # Here I am pointing to my custom templates for the blog title and blog description, I will talk about these in a little.
    title_template = '_feeds/blog_title.html'
    description_template = '_feeds/blog_description.html'

    # This pulls the blog.model's charfield "author" so that the author's name can be dynamic (I just did this to future proof).
    def item_author_name(self, item):
        return item.author

    def items(self):
        return Article.objects.filter(enabled=True).order_by('-created')[:10]

    def item_pubdate(self, item):
        return item.created

