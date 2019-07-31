from django.urls import path
from . import views
from django.conf.urls import url,include
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    url(r'^football/$',views.football, name='football'),
    url(r'^bookmakers/$',views.bookmakers, name='bookmakers'),
    url(r'^codespromos/$',views.codespromos,name='codespromos'),

]
