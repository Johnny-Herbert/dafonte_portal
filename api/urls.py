from django.urls import path, include
from api import views

urlpatterns = [
    path("members/lawyers", views.lawyerList, name="lawyer-list"),
    path("members/adms", views.admList, name="adm-list"),
    path("members/treinee", views.treineeList, name="treinee-list"),
    path("members/intern", views.internList, name="intern-list"),
]