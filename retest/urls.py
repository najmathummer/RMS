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
	url(r'^event/$', views.login_user, name= 'login_user'),
	url(r'^event/eventclassroomform/$',views.EventclassroomCreate.as_view(), name='eventclassroomform'),
	url(r'^event/eventauditoriumform/$',views.EventauditoriumCreate.as_view(), name='eventauditoriumform'),
	url(r'^event/eventextensioncableform/$',views.EventextensioncableCreate.as_view(), name='eventextensioncableform'),
	url(r'^event/eventgraphicshallform/$',views.EventgraphicshallCreate.as_view(), name='eventgraphicshallform'),
	url(r'^event/eventlabform/$',views.EventlabCreate.as_view(), name='eventlabform'),
	url(r'^event/eventmikesystemform/$',views.EventmikesystemCreate.as_view(), name='eventmikesystemform'),
	url(r'^event/eventprojectorform/$',views.EventprojectorCreate.as_view(), name='eventprojectorform'),
	

	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/ashokdetails$' , views.ashokdetails, name='ashokdetails' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/ashokaccept$' , views.ashokaccept, name='ashokaccept' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/ashokretreq$' , views.ashokretreq, name='ashokretreq' ),

	
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectordetails$' , views.projectordetails, name='projectordetails' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectoraccept$' , views.projectoraccept, name='projectoraccept' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectorretreq$' , views.projectorretreq, name='projectorretreq' ),
	
	url(r'^event/(?P<eventlab_id>[0-9]+)/labdetails$' , views.labdetails, name='labdetails' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labaccept$' , views.labaccept, name='labaccept' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labretreq$' , views.labretreq, name='labretreq' ),
	
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditoriumdetails$' , views.auditoriumdetails, name='auditoriumdetails' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditoriumaccept$' , views.auditoriumaccept, name='auditoriumaccept' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditretreq$' , views.auditretreq, name='auditretreq' ),
	
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikedetails$' , views.mikedetails, name='mikedetails' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikeaccept$' , views.mikeaccept, name='mikeaccept' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikeretreq$' , views.mikeretreq, name='mikeretreq' ),
	
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classroomdetails$' , views.classroomdetails, name='classroomdetails' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classroomaccept$' , views.classroomaccept, name='classroomaccept' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classroomretreq$' , views.classroomretreq, name='classroomretreq' ),
	
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cabledetails$' , views.cabledetails, name='cabledetails' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cableaccept$' , views.cableaccept, name='cableaccept' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cableretreq$' , views.cableretreq, name='cableretreq' ),



	
]