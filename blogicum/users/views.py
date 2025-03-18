from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import MyUserForm
from .models import MyUser


# Create your views here.

