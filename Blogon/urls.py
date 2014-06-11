from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blogon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^blog/(?P<slug>[\w\-/w]+)/', 'blog.views.blog_view',name ='blog_view'),
    url(r'^admin/', include(admin.site.urls)),
)
