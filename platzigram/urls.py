#ESTE ARCHIVO RELACIONA URLS CON SUS VISTAS CORRESPONDIENTES
#ds: Una vista en Django es una función!

#from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views



#ds: Todas las vistas reciben un "request"


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-world', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/', posts_views.list_posts),
]
