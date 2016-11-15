from django.db import models
from django_comments.models import BaseCommentAbstractModel

class MyCommentsModel(BaseCommentAbstractModel):
	text = models.CharField(max_length=800)