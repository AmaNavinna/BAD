from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # maps to the index view for the home path
    path('home/', views.index, name='home'),
    path('movies/', views.movies, name='movies'),
    path('now_showing/<int:now_showing_id>/', views.now_showing_details, name='movie_details'),
    path('upcoming/<int:upcoming_id>/', views.upcoming_details, name='uocoing_details'),
    path('transaction/', views.transaction_view, name='transaction'),
    path('contactus/', views.contact_us, name='contact_us'),

]