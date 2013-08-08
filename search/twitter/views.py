from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from models import Author, Tweet


class TweetList(ListView):
    paginate_by = 10
    model = Tweet

    def get_queryset(self):
        term = self.request.REQUEST.get('search')

        if term:
            return self.model.objects.filter(text__icontains=term)
        else:
            return self.model.objects.all()
