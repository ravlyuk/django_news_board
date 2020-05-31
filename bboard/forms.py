from django.forms import ModelForm

from .models import Bb, Comment


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ("title", "content", "name_author", "rubric")


class BbComment(ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "content")
