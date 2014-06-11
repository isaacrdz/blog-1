from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blogon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/(?P<slug>[\w\-/w]+)/', 'blog.views.blog_view',name ='blog_view'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
