from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'nonilnil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'webapp/', include('webapp.urls')),
    # https://django-registration-redux.readthedocs.org/en/latest/
    url(r'^accounts/', include('registration.backends.default.urls')),
]

