from django.conf.urls import patterns, include, url
from splunkdj.utility.views import render_template as render

urlpatterns = patterns('',
    url(r'^home/$', 'fileUpload.views.home', name='home'),
)

# urlpatterns = patterns('',
#     url(r'^upload/$', 'fileUpload.views.upload', name='upload'),
# )
