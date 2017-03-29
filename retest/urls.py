from django.conf.urls import url
from . import views
urlpatterns = [
	
	url(r'^retest/$', views.login_user, name='login_user'),
	url(r'^$', views.login_user, name='login_user'),
	
	url(r'^retest/retestform/$',views.RetestCreate.as_view(), name='retestform'),
	url(r'^retest/(?P<retest_id>[0-9]+)/$' , views.details, name='details' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/accept$' , views.accept, name='accept' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/request$' , views.request, name='request' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/accepted$' , views.accepted, name='accepted' ),
	url(r'^retest/(?P<retest_id>[0-9]+)/retreq$' , views.retreq, name='retreq' ),


	
]