from django.conf.urls import include, url
from django.contrib import admin
from novnc import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_noVNC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vnc/$', views.run_vnc),
]
