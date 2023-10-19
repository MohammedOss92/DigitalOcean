from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('home', views.index, name='home'),
    path('img_type/', views.create_img_type, name='create_img_type'),
    path('add_img/', views.add_img_withTypeType, name='add_img_withTypeType'),
    path('imgtypes_api/', views.imgtypes_api),
    path('imgsapi/<int:id>' , views.imgsapi),
]