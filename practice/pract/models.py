from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200,default='user',help_text="User Name not greater Than 200 character")
    password = models.CharField(max_length=200,verbose_name="Enter your Password")
    nickName = models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.name


class Musician(models.Model):
    first_name = models.CharField(max_length=50,db_column='Musician First Name',db_index=True)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    numberOfExperience = models.CharField(max_length=200,blank=True,editable=False)

    def __str__(self):
        return self.first_name

class Album(models.Model):
    BOOK_TYPE = (
        ('F', 'Fantisy'),
        ('FS', 'Sciencce Fiction'),
    )
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    # type = models.CharField(max_length=10,choices=BOOK_TYPE)

    class meta:
        abstract = True
        db_table = 'music_album'
        # app_label = "pract"
        # constraints = [models.checkConstraint(check = models.Q(len(name).__gte == 10))]

    def __str__(self):
        return self.artist


class Singer(Album,models.Model):
    medalType = models.TextChoices('MedalType','GOLD SILVER BRONZE')
    def __str__(self):
        self.name

