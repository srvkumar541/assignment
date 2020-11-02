# from django.urls import include, path
# from rest_framework import routers
# from myproject.api import views
# from rest_framework.authtoken.views import ObtainAuthToken
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('auth/', ObtainAuthToken.as_view()),
# ]
from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
]