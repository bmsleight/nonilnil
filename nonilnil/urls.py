from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'nonilnil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'webapp/', include('webapp.urls')),
    # https://django-registration-redux.readthedocs.org/en/latest/
    url(r'^accounts/', include('registration.backends.default.urls')),

        #override the default urls
    url(r'^password/change/$',
                auth_views.password_change,
                name='password_change'),
    url(r'^password/change/done/$',
                auth_views.password_change_done,
                name='password_change_done'),
    url(r'^password/reset/$',
                auth_views.password_reset,
                name='password_reset'),
    url(r'^password/reset/done/$',
                auth_views.password_reset_done,
                name='password_reset_done'),
    url(r'^password/reset/complete/$',
                auth_views.password_reset_complete,
                name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                auth_views.password_reset_confirm,
                name='password_reset_confirm'),

]

