from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
	
	url(r'^retest/$', views.login_user, name='login_user'),

	url(r'^$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^retest/homepage/$', views.homepage, name='rms'),
	
	
	url(r'^retest/retestform/$',login_required(views.RetestCreate.as_view()), name='retestform'),
	url(r'^retest/(?P<retest_id>[0-9]+)/$' , views.details, name='details' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/accept$' , views.accept, name='accept' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/request$' , views.request, name='request' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/accepted$' , views.accepted, name='accepted' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/retreq$' , views.retreq, name='retreq' ),


	
]