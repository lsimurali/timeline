from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    image_url=models.CharField(max_length=350)
    created_by=models.CharField(max_length=50)

    class Meta():
        db_table='posts'

class Document(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE ,default=1)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'Document'

class Like(models.Model):
    post = models.ForeignKey(Document,on_delete=models.CASCADE)
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField()

    class Meta():
        db_table = 'Like'




class Comment(models.Model):
    post = models.ForeignKey(Document,on_delete=models.CASCADE)
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)

    class Meta():
        db_table = 'Comment'