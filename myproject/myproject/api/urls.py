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
from .views import RegisterAPI,LoginAPI, FileUploadView
from django.urls import path
from knox import views as knox_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/fileUpload/', FileUploadView.as_view(), name='fileUpload')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)