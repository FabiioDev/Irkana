
from django.contrib import admin
from django.urls import path

from core.erp.views import myFirstView, mySecondView

app_name = 'erp'

urlpatterns = [
    path('prueba/', admin.site.urls),
    path('uno/', myFirstView, name='vista1'),
    path('dos/', mySecondView, name='vista2')
]