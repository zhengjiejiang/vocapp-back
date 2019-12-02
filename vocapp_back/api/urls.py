from django.urls import path

from . import views

urlpatterns = [



# ---- homepage -----

    path('api/version', views.api_version, name='api_version'),
# ---- gateway-----

    path('api/regsiter', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', views.LoginAPI.as_view(), name='login_api'),
    path('api/logout', views.post_logout_api, name='logout_api'),


]
