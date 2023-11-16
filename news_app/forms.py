from django.forms import ModelForm, HiddenInput
from .models import ContactMessage, Comment, ReplyComment


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class ReplyCommentCreateForm(ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['reply_comment']
