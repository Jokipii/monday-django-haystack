from django import forms


class TweetSearchForm(forms.Form):
    search = forms.CharField()
