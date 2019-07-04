from django.db import models

# Create your models here.

class User(models.Model):

    class Meta:

        db_table = 'user'

    id       = models.AutoField(primary_key = True)
    name     = models.CharField(max_length = 48, null = False)
    email    = models.CharField(max_length = 48, null = False)
    password = models.CharField(max_length = 128, null = False)
    time     = models.DateTimeField(auto_now_add=True)
    idDelete = models.BooleanField(default=False)

    def __repr__(self):
        return "{},{}".format(self.id,self.name)

    __str__ = __repr__
    
class Content(models.Model):

    class Meta:

        db_table = 'content'

    id        = models.AutoField(primary_key = True)
    type      = models.CharField(max_length = 48, null = False)
    title     = models.CharField(max_length = 48, null = False)
    content   = models.TextField(max_length = 65535, null = False)
    tag       = models.CharField(max_length = 48, null = False)
    firsttime = models.DateTimeField(auto_now_add=True)
    lasttime  = models.DateTimeField(auto_now_add=True)
    isDelete  = models.BooleanField(default=False)

    def __repr__(self):
        return "{},{},{}".format(self.id,self.title,self.tag)

    __str__ = __repr__
