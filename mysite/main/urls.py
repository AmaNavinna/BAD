from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # maps to the index view for the home path
    path('home/', views.index, name='home'),
    path('movies/', views.movies, name='movies'),
    path('movie/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('transaction/<int:movie_id>/', views.transaction, name='transaction'),
    path('contactus/', views.contact_us, name='contact_us'),

]