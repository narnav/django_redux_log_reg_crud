from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from  . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('about/', views.about),
    path('contact/', views.contact),
    path("products", views.MyModelView.as_view()),
    path("products/<pk>", views.MyModelView.as_view()),

]