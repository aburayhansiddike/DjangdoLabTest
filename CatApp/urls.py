from django.urls import path, include
from CatApp import views

urlpatterns = [
    path('cat/', views.CatList.as_view(), name="catList"),
    path('cat/<int:pk>', views.CatDetails.as_view(), name="catDetails")
]
