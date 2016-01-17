from django.conf.urls import url
from . import views

    # url(r'^blog/', include('blog.urls')),

# / 	               List of all Series, highest PK first
# /?P<pk>[0-9]+/       The series showing round by round, highest round PK first
# /?P<pk>[0-9]+/       

urlpatterns = [
    url(r'^$', views.series_list, name='series_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.series_detail, name='series_detail'),
    url(r'^(?P<s_pk>[0-9]+)/(?P<r_pk>[0-9]+)/prediction/$', views.manage_prediction, name='manage_prediction'),
    url(r'^(?P<pk>[0-9]+)/l/$', views.loser_detail, name='loser_detail'),
    url(r'^(?P<s_pk>[0-9]+)/(?P<r_pk>[0-9]+)/nilnils/$', views.manage_nilnils, name='manage_nilnils'),
    url(r'^(?P<s_pk>[0-9]+)/(?P<r_pk>[0-9]+)/missing/$', views.missing_prediction, name='missing_prediction'),
    url(r'^(?P<s_pk>[0-9]+)/(?P<r_pk>[0-9]+)/ping/$', views.ping_email_message, name='ping_email_message'),
]
