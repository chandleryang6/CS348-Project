from django.urls import path
from . import views

#urlpatterns: A list of URL patterns for the application. 
#It maps URLs to their corresponding view functions in 'views.py'.
urlpatterns = [
    path("", views.home, name="home"),
    path('delete_concert/<int:concert_id>/', views.delete_concert, name='delete_concert'),
    path('edit_concert/<int:concert_id>/', views.edit_concert, name='edit_concert'),
    path('view_concerts/', views.view_concerts, name='view_concerts'),  
]
