from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('itinerary_form/', views.itinerary_generate, name='itinerary_generate'),
    path('', views.guest_mode, name='guest_mode'),
    path('logout/', views.logout, name='logout'),
]
