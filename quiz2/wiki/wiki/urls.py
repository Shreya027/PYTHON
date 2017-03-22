"""wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from wikiapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^start/', views.question1),
    url(r'^audi/', views.question2),
    url(r'^choux_pastry/', views.question3),
    url(r'^gold_frankincense_myrrh/', views.question4),
    url(r'^good_will_hunting/', views.question5),
    url(r'^mishipeshu/', views.question6),
    url(r'^main_quad/', views.end),



]


if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
