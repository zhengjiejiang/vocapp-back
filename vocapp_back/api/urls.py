from django.urls import path

from . import views

urlpatterns = [



# ---- gateway-----

    path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', views.LoginAPI.as_view(), name='login_api'),
    path('api/logout', views.LogoutAPI.as_view(), name='logout_api'),

# ---- Dashboard----
    path('api/voc_add', views.VocAddAPI.as_view(), name='register_api'),



]
