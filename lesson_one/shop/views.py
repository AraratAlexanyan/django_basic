from django.shortcuts import HttpResponse


def index(req):
    return HttpResponse("Buy and sell something")


def buy(req, page_id):
    return HttpResponse(f'Search and buy, page{page_id}')


def sell(req):
    return HttpResponse('Sell your products')

