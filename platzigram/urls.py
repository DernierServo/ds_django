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
from platzigram import views



#ds: Todas las vistas reciben un "request"


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-world', views.hello_world),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
