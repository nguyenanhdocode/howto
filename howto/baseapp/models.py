from configparser import MAX_INTERPOLATION_DEPTH
from email.policy import default
from sre_constants import CATEGORY_NOT_DIGIT
from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
from taggit.models import Tag

from ckeditor_uploader.fields import RichTextUploadingFormField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    title = models.TextField(max_length=255)
    content = RichTextUploadingFormField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    liked = models.ManyToManyField(get_user_model())
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = Tag()