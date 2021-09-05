from django.shortcuts import render
from django.db import transaction
# Create your views here.

@transaction.non_atomic_requests
def getUser(request):
    pass

transaction.on_commit()