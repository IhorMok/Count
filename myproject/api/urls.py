from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import accountant_record, \
                   accountant_record_new, \
                   account_record_delete






urlpatterns = [
    path('', accountant_record),
    path('new', accountant_record_new),
    path("<int:id>/", account_record_delete),



    #path('new/redirect', redirect_views),


    #path('index/', include('api.accountant_record')),
]
