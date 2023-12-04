from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),  # maps to the index view for the home path
    path('home/', views.index, name='home'),
    path('movies/', views.movies, name='movies'),
    path('transaction/', views.transaction_view, name='transaction'),
    path('contactus/', views.contact_us, name='contact_us'),
    #path('movie_details/<str:movie_type>/<int:movie_id>/', views.movie_details, name='movie_details'),


]