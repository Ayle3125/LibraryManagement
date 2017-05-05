from django.db import models
from django.contrib.auth.models import User
import datetime
class MyUser(models.Model):
        user = models.OneToOneField(User)
        nickname = models.CharField(max_length = 16)
        school_ID = models.CharField(max_length = 10,default = '') 
        permission = models.IntegerField()

        def __unicode__(self):
            return self.user.username

class Book(models.Model):
        name = models.CharField(max_length = 128)
        price = models.FloatField()
        author = models.CharField(max_length = 128)
        pubDate = models.DateField()
        typ = models.CharField(max_length = 128)
        STATUS = (
                (u'Available',u'Available'),
                (u'Borrowed',u'Borrowed'),
                )
        status = models.CharField(max_length=20,choices=STATUS,default='Available')
        num = models.IntegerField(max_length=11,default = 1)
        class META:
            ordering = ['name']

        def __unicode__(self):
            return self.name

class Img(models.Model):
        name = models.CharField(max_length = 128)
        desc = models.TextField()
        img = models.ImageField(upload_to = 'image')
        book = models.ForeignKey(Book)

        class META:
            ordering = ['name']

        def __unicode__(self):
            return self.name


class Record(models.Model):
        book = models.ForeignKey(Book)
        user = models.ForeignKey(MyUser)
        borrow_time = models.DateTimeField(default =datetime.datetime.today() )
        should_back_time = models.DateTimeField( default =datetime.datetime.today()+datetime.timedelta(days=30) )
        real_back_time = models.DateTimeField(null=True)
        state = models.IntegerField(default = 0)# 0:ing, -1:rejected, -2:back over, 1:borrow, 2:reborrow, 3:give_back;

