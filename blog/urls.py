from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('info_detail',views.info_detail,name='info_detail'),
    path('post_list',views.post_list,name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/',views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('info_edit',views.info_edit,name='info_edit'),
    path('admin',views.post_admin, name='post_admin'),
]
