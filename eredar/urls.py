"""eredar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from eredar import settings
from reader import views

urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
    url(r'^upload/', views.book_upload_form, name='upload'),
    url(r'reader/(\d+)', views.epub_read, name='reader'),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
