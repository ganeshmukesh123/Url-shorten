from django.urls import path,re_path
from . import views

urlpatterns = [
    
    re_path(r'^app$',views.index,name="index"),
    path('create',views.create,name="create"),
    # re_path(r'^\w+|',views.getActual,name="getActual")
    path('notfound/',views.notFound,name="notfound"),
    path('<str:pk>',views.getActual,name="getActual")
]