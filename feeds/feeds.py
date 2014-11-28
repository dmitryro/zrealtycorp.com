from django.contrib.syndication.views import Feed
from property.models import Property
from django.utils.feedgenerator import Atom1Feed


class RssSiteNewsFeed(Feed):
    title = "ZRealty Corp site news"
    link = "/feeds/"
    description = "Latest Feeds"


    def get_context_data(self, **kwargs):
        context = super(RssSiteNewsFeed, self).get_context_data(**kwargs)
        return context

    def item_link(self, item):
        """
        Takes an item, as returned by items(), and returns the item's URL.
        """
        return 'http://zrealtycorp.com/property/' + str(item.property_id)
   

    def items(self):
        properties =  Property.objects.order_by('-published')[:5]
        return properties


class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description
