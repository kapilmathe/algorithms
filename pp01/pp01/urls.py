from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from filebrowser import sites


urlpatterns = [
    # Examples:
    # url(r'^$', 'pp01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    # path('admin/filebrowser/', sites.site.urls),
]
