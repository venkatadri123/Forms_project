from django.urls import path
from App_forms import views

urlpatterns = [
    path('',views.contact),
    path('snippet/',views.snippet_detal)
]