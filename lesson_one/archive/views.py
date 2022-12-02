import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import HttpResponse, redirect


def index(req, year):

    if year > datetime.datetime.now().year:
        return HttpResponseNotFound(f'<h1>Oops. Wrong data Page not found for year <i>{year}</i></h1>')

    if year < 2000:
        return redirect('/archive', permanent=False)

    if year < 2011:
        return HttpResponseNotFound(f'<h1>Archive for year <i>{year} already deleted</i></h1>')

    return HttpResponse(f'<h1>Archive data by year <i>{year}</i></h1>')


def main_page(req):
    return HttpResponse('Archive by years')
