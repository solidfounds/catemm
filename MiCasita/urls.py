"""MiCasita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls import patterns, url
from users.views import userlogin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', 'app.views.primerRegistro', name='agregar_clientes'),
    url(r'^nota_remision/', 'app.views.nota_remision', name='nota'),
    url(r'^clientes/', 'app.views.clientes', name='clientes'),
    url(r'^desempeno/', 'app.views.desempeno', name='desempeno'),

    url(r'^$', userlogin.as_view(), name='login'),
    	#url(r'^$', 'users.views.userlogin', name='login'),
	url(r'^salir/$', 'users.views.LogOut', name='logout')

]




from django.conf import settings

# ... your normal urlpatterns here
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})


        )