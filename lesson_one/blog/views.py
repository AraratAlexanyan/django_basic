from django.shortcuts import HttpResponse

# Create your views here.


def index(req):

    return HttpResponse('Blog main page')


def ask(req):
    return HttpResponse("Ask something here")


def questions(req):
    return HttpResponse('<h1>Questions page</h1>')

