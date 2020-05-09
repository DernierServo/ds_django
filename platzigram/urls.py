#ESTE AARCHIVO RELACIONA URLS CON SUS VISTAS CORRESPONDIENTES
"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


#ds: Una vista en Django es una función!

#from django.contrib import admin
from django.urls import path
#ds: para escribir una respuesta en Django:
from django.http import HttpResponse



#ds: Todas las vistas reciben un "request"
def hello_world(request):
    return HttpResponse('Hello, world from DServo Labs')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-world', hello_world )
]
