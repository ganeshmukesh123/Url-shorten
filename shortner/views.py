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
        urlExist = checkUrlExist(url)
        uid = ""
        if urlExist:
            # print("exist")
            existUrl = Url.objects.get(url=url)
            uid = existUrl.uuid
        else:
            # print("not exist")
            uid = str(uuid.uuid4())[:8]
            if checkUuidExist(uid):
                uid = str(uuid.uuid4())[:8]
                
            newUrl = Url(url=url,uuid=uid)
            newUrl.save()

        return JsonResponse({'status':'success','data':{'alias':uid}})
    else:
        return JsonResponse({'status':'fail'})

def getActual(request,pk):
    print('getActual')
    if checkUuidExist(pk):
        # genrating url
        existUrl = Url.objects.get(uuid=pk)
        return redirect(existUrl.url)
    else:
        # not found
        return redirect('/notfound/')
    
    
    # return redirect('https://www.djangoproject.com/')

def checkUrlExist(url):
    response = Url.objects.filter(url=url)
    if not response.exists():
        return False
    else:
        return True

def checkUuidExist(uid):
    response = Url.objects.filter(uuid=uid)
    if not response.exists():
        return False
    else:
        return True

def notFound(request):
    return render(request,'404notfound.html')