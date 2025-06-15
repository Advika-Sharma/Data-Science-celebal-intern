from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', views.members_list, name='members'),
]