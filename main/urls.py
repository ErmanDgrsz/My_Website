from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.layout, name='layout'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]

urlpatterns += staticfiles_urlpatterns()
