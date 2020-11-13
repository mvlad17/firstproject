from django.http import HttpResponse
from django.shortcuts import render


def page(request):
    return render(request, 'page.html', {'greeting': 'Hello!'})

# TODO сделать что-то
