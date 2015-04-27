from django.conf.urls import patterns, include, url
from django.contrib import admin


<<<<<<< HEAD
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('app.urls')),
=======
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('app.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

>>>>>>> 4a019b9aef590ef3439be748c275eeaaafae660d
)
