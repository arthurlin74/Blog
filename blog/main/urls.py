from django.urls import path
from main import views


app_name = 'main'
<<<<<<< HEAD

urlpatterns = [
    path('',views.main, name='main'),
    path('about/',views.about,name='about')
]

=======
urlpatterns = [
    path('', views.main, name='main'),
]
>>>>>>> branch 'master' of https://github.com/arthurlin74/blog
