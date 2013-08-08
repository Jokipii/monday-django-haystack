from haystack import indexes
from models import Tweet


class TweetIndex(indexes.SearchIndex, indexes.Indexable):
    created_date = indexes.DateTimeField(model_attr='created_at')
    source = indexes.CharField()
    text = indexes.CharField(document=True)
    location_name = indexes.CharField()
    country = indexes.CharField()

    def get_model(self):
        return Tweet

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
