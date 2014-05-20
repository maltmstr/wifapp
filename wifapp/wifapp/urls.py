from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from wifapp import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'wifapp.views.index', name='index'),
	#url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls', namespace="polls")),
)
