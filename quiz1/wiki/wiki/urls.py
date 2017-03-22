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
    url(r'^070317/', views.question2),
    url(r'^7/', views.question3),
    url(r'^maid/', views.question4),
    url(r'^choux_pastry/', views.question5),
    url(r'^-#o-#o-#o/', views.question6),
    url(r'^country/', views.question7),
    url(r'^audi/', views.question8),
    url(r'^gold_frankincense_myrrh/',views.question9),
    url(r'^baidu/', views.question10),
    url(r'^good_will_hunting/', views.question11),
    url(r'^main_quad/', views.question12),
    url(r'^horseshoe/', views.question13),
    url(r'^0.25/', views.question14),
    url(r'^time/', views.end),
]


if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
