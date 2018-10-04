from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from mobility import utils
import os

boto_key = os.environ.get("BOTO_PUB_KEY")
boto_s_key = os.environ.get("BOTO_SECRET_KEY")

# @login_required
def index(request):
    return render(request, 'mobility/index.html')


def cards(request):
  return render(request, 'mobility/cards.html')
