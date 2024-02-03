# -*- encoding: utf-8 -*-
import time
from django.views.generic import ListView

import re
from datetime import date, timedelta
from django.urls import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


@login_required(login_url="login")
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context=context)


def custom_page_not_found_view(request, exception):
    return redirect('home')


def custom_error_view(request, exception=None):
    return redirect('home')


def custom_permission_denied_view(request, exception=None):
    return redirect('home')


def custom_bad_request_view(request, exception=None):
    return redirect('home')
