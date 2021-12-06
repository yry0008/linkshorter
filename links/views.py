from random import randint
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from links.models import link
# Create your views here.

def index(request, token):
    #return HttpResponse(token)
    try:
        l = link.objects.get(token=token)
    except link.DoesNotExist:
        raise Http404("Link does not exist")
    url = l.redirect
    return render(request, 'index.html', {'url': url})

def create(request):

    return HttpResponse('create')
    return render(request, 'create.html')

def do_create(request):
    token = request.POST.get("token")
    if token == None or token == "":
        import random
        token = "".join([chr(random.randint(1,65535)%26+97) for i in range(8)])
    return HttpResponse(token)