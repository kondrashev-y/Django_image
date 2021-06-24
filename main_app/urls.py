from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.list_image_view),
    path('upload/', views.image_upload_view),
    path('detail/<int:pk>', views.detail_image_view, name='detail'),
]