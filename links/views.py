from random import randint
import configloader
import time
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from links.models import link
# Create your views here.

def index(request, token):
    #return HttpResponse(token)
    try:
        l = link.objects.get(token=token)
        l.count += 1
        l.save()
    except link.DoesNotExist:
        raise Http404("Link does not exist")
    url = l.redirect
    return render(request, 'index.html', {'url': url})

def create(request):
    return render(request, 'create.html',{'baseurl':configloader.config().getkey("baseurl")})

def do_create(request):
    c = configloader.config()
    token = request.POST.get("token")
    redirect = request.POST.get("redirect")
    if token in ["admin","do_create","do_delete","index","stat"]:
        return JsonResponse({'ret':0, 'msg':'Invalid token'})
    if token == None:
        import random
        token = "".join([chr(random.randint(1,65535)%26+97) for i in range(8)])
    token = token.replace(" ","")
    if token == "":
        import random
        token = "".join([chr(random.randint(1,65535)%26+97) for i in range(8)])

    try:
        l = link.objects.get(token=token)
        return JsonResponse({'ret':0, 'msg':'token already exists'})
    except link.DoesNotExist:
        pass
    l = link()
    l.token = token
    l.redirect = redirect
    l.create_time = int(time.time())
    import random
    l.del_token = "".join([chr(random.randint(1,65535)%26+97) for i in range(20)])
    l.save()
    return JsonResponse({'ret':1, 'msg':'success', 'baseurl':c.getkey("baseurl"),'token':token, 'del_token':l.del_token})

def do_delete(request):
    token = request.GET.get("token")
    if token == None or token == "":
        return JsonResponse({'ret':0, 'msg':'Invalid token'})
    try:
        l = link.objects.get(del_token=token)
    except link.DoesNotExist:
        return JsonResponse({'ret':0, 'msg':'token does not exist'})
    l.delete()
    return JsonResponse({'ret':1, 'msg':'success'})