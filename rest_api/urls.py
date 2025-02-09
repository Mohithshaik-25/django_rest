from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/rest-prac/', views.RestPracListCreateView.as_view(), name="rest-prac-list-create"),
    path('api/rest-prac/<int:pk>/', views.RestPracDetailView.as_view(), name="rest-prac-detail"),
    path('register',views.register,name="register"),
    path('update',views.update,name="update"),

]
