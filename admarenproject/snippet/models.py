from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    id       = models.AutoField(primary_key=True)
    title    = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table='Tag'

class Snippet(models.Model):
    id         = models.AutoField(primary_key=True)
    title      = models.CharField(max_length=255)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    tag        = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        db_table='snippet'

class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    class Meta:
        db_table='login'


