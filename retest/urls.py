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
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/ashokindetails$' , views.ashokindetails, name='ashokindetails' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/ashokhdetails$' , views.ashokhdetails, name='ashokhdetails' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/gaccept$' , views.gaccept, name='gaccept' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/iaccept$' , views.iaccept, name='iaccept' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/haccept$' , views.haccept, name='haccept' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/ashokretreq$' , views.ashokretreq, name='ashokretreq' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/ashokwretreq$' , views.ashokwretreq, name='ashokwretreq' ),
	url(r'^event/(?P<eventgraphicshall_id>[0-9]+)/graphicswithdraw$' , views.graphicswithdraw, name='graphicswithdraw' ),

	
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectordetails$' , views.projectordetails, name='projectordetails' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectoraccept$' , views.projectoraccept, name='projectoraccept' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectorindetails$' , views.projectorindetails, name='projectorindetails' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/iprojectoraccept$' , views.iprojectoraccept, name='iprojectoraccept' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectorhdetails$' , views.projectorhdetails, name='projectorhdetails' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/hprojectoraccept$' , views.hprojectoraccept, name='hprojectoraccept' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectorretreq$' , views.projectorretreq, name='projectorretreq' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectorhretreq$' , views.projectorhretreq, name='projectorhretreq' ),
	url(r'^event/(?P<eventprojector_id>[0-9]+)/projectorrecieved$' , views.projectorrecieved, name='projectorrecieved' ),
	
	url(r'^event/(?P<eventlab_id>[0-9]+)/labdetails$' , views.labdetails, name='labdetails' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labaccept$' , views.labaccept, name='labaccept' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labindetails$' , views.labindetails, name='labindetails' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/ilabaccept$' , views.ilabaccept, name='ilabaccept' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labhdetails$' , views.labhdetails, name='labhdetails' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/hlabaccept$' , views.hlabaccept, name='hlabaccept' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labretreq$' , views.labretreq, name='labretreq' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labwretreq$' , views.labwretreq, name='labwretreq' ),
	url(r'^event/(?P<eventlab_id>[0-9]+)/labwithdraw$' , views.labwithdraw, name='labwithdraw' ),
	
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditoriumdetails$' , views.auditoriumdetails, name='auditoriumdetails' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditoriumaccept$' , views.auditoriumaccept, name='auditoriumaccept' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditoriumindetails$' , views.auditoriumindetails, name='auditoriumindetails' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/iauditoriumaccept$' , views.iauditoriumaccept, name='iauditoriumaccept' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditoriumhdetails$' , views.auditoriumhdetails, name='auditoriumhdetails' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/hauditoriumaccept$' , views.hauditoriumaccept, name='hauditoriumaccept' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditretreq$' , views.auditretreq, name='auditretreq' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditwretreq$' , views.auditwretreq, name='auditwretreq' ),
	url(r'^event/(?P<eventauditorium_id>[0-9]+)/auditwithdraw$' , views.auditwithdraw, name='auditwithdraw' ),
	
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikedetails$' , views.mikedetails, name='mikedetails' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikeaccept$' , views.mikeaccept, name='mikeaccept' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikeindetails$' , views.mikeindetails, name='mikeindetails' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/imikeaccept$' , views.imikeaccept, name='imikeaccept' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikehdetails$' , views.mikehdetails, name='mikehdetails' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/hmikeaccept$' , views.hmikeaccept, name='hmikeaccept' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikeretreq$' , views.mikeretreq, name='mikeretreq' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikehretreq$' , views.mikehretreq, name='mikehretreq' ),
	url(r'^event/(?P<eventmikesystem_id>[0-9]+)/mikerecieved$' , views.mikerecieved, name='mikerecieved' ),
	
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classroomdetails$' , views.classroomdetails, name='classroomdetails' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classroomaccept$' , views.classroomaccept, name='classroomaccept' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classroomidetails$' , views.classroomidetails, name='classroomidetails' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/iclassroomaccept$' , views.iclassroomaccept, name='iclassroomaccept' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classretreq$' , views.classretreq, name='classretreq' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classwretreq$' , views.classwretreq, name='classwretreq' ),
	url(r'^event/(?P<eventclassroom_id>[0-9]+)/classwithdraw$' , views.classwithdraw, name='classwithdraw' ),
	
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cabledetails$' , views.cabledetails, name='cabledetails' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cableaccept$' , views.cableaccept, name='cableaccept' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cableindetails$' , views.cableindetails, name='cableindetails' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/icableaccept$' , views.icableaccept, name='icableaccept' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cablehdetails$' , views.cablehdetails, name='cablehdetails' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/hcableaccept$' , views.hcableaccept, name='hcableaccept' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cableretreq$' , views.cableretreq, name='cableretreq' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cablehretreq$' , views.cablehretreq, name='cablehretreq' ),
	url(r'^event/(?P<eventextensioncable_id>[0-9]+)/cablerecieved$' , views.cablerecieved, name='cablerecieved' ),






	
]