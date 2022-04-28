from xml.etree.ElementTree import Comment
from django.forms import ModelForm


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']