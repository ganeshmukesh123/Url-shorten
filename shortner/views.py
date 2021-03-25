from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.conf import settings
import uuid
from .models import Url
from django.http import JsonResponse

# Create your views here.
def index(request):
    # print(settings.BASE_DIR)
    return render(request,'index.html')

def create(request):
    # print('create')
    # print(request)
    if request.method == 'POST':
        url = request.POST['url']
        uid = str(uuid.uuid4())[:8]
        # print(uid)
        newUrl = Url(url=url,uuid=uid)
        newUrl.save()
        return JsonResponse({'status':'success','data':{'alias':uid}})
    else:
        return JsonResponse({'status':'fail'})

def getActual(request):
    print('getActual')
    # return HttpResponse('getActual')
    return redirect('https://www.djangoproject.com/')

