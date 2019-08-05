from django.urls import path
from .views import *

urlpatterns = [
path('', index),

path('login/', login),
path('admin/', admin),
path('logout/', logout),

path('upload/', upload),

path('article/', article),
path('article/<int:id>/', detail),

path('article/tecnology/', article_tecnology),
path('article/lifestyle/', article_lifestyle),

path('image/', image),
path('image/<int:id>/', detail),

path('voice/', voice),
path('voice/<int:id>/', detail),

path('tag/<str:tags>/', tag),

path('about/', about),

]