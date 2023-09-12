# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('contents/', views.ContentListView.as_view(), name='content-list'),
    path('contents/<int:pk>/', views.ContentDetailView.as_view(), name='content-detail'),
    path('search/', views.ContentSearchView.as_view(), name='content-search'),
]
