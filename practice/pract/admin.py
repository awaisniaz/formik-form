from django.contrib import admin
from .models import User,Album,Musician,Singer
# Register your models here.
admin.site.register([User,Album,Musician,Singer])