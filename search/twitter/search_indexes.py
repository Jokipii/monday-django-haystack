from haystack import indexes
from models import Tweet


class TweetIndex(indexes.SearchIndex, indexes.Indexable):
    created_date = indexes.DateTimeField(model_attr='created_at')
    source = indexes.CharField(model_attr='source')
    text = indexes.EdgeNgramField(model_attr='text', document=True, use_template=True)
    country = indexes.EdgeNgramField(model_attr='country', null=True)
    author = indexes.CharField(model_attr='author')

    def prepare_author(self, obj):
        return obj.author.name or ''

    def get_model(self):
        return Tweet
