from django import forms
from django_comments.forms import CommentForm
from mycomments.models import MyCommentsModel

class MyCommentsForm(CommentForm):
	text = forms.CharField(widget=forms.Textarea)

	def get_comment_create_data(self):
		data = super(MyCommentsForm, self).get_comment_create_data()
		data['text'] = self.cleaned_data['text']
		return data
