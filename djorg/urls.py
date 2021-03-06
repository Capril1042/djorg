"""djorg URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from rest_framework import routers
from notes.api import NoteViewSet
from djorg import views as core_views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

urlpatterns = [
    path('accounts/', include ('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api2/', include('blog.urls')),
    path('bookmarks/', include('bookmarks.urls')),
    path('contacts/', include('contacts.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', TemplateView.as_view(template_name='djorg_base.html')),
    path('notes/', TemplateView.as_view(template_name="index.html")),
    path('oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]
