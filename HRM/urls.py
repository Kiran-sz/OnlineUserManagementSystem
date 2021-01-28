from django.urls import path

from .views import UserList

from HRM import views

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<employee_id>', views.UserDetails.as_view()),
]