from django.http import HttpResponse
from django.shortcuts import render, redirect

from .celery import example_task


def index(request):
    context = {}
    return render(request, "accounts/login.html", context=context)


def health_check(request):
    return HttpResponse("OK")


def test_task(request):
    example_task.delay()
    return HttpResponse("Task triggered, see Celery logs")
