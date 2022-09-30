from email import contentmanager
from email.policy import default
from ssl import create_default_context
from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(default=' ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
