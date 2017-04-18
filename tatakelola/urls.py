from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import login, logout


urlpatterns =[
	url(r'^login/$', login, {}, 'login'),
	url(r'^logout/$', logout, {}, 'logout'),
	url(r'^notifications/$', views.notifications, {'template_name': 'tatakelola/notifications.html'}, 'notifications'),
    url(r'^notifications_mark_all_as_read/$', views.notifications_mark_all_as_read, {}, 'notifications_mark_all_as_read'),
    url(r'^step1/$', views.step1, {'template_name': 'tatakelola/step1.html'}, 'step1'),
    url(r'^step2/$', views.step2, {'template_name': 'tatakelola/step2.html'}, 'step2'),
    url(r'^step3/$', views.step3, {'template_name': 'tatakelola/step3.html'}, 'step3'),
    url(r'^step4/$', views.step4, {'template_name': 'tatakelola/step4.html'}, 'step4'),
    url(r'^step5/$', views.step5, {'template_name': 'tatakelola/step5.html'}, 'step5'),
    url(r'^$', TemplateView.as_view(template_name="tatakelola/home.html"), {}, 'home'),
    url(r'^user_dashboard/$', views.user_dashboard, {'template_name': 'tatakelola/user_dashboard.html'}, 'user_dashboard'),
    url(r'^user/$', views.user, {'template_name': 'tatakelola/userform.html'}, 'user'),
    url(r'^proyek_dashboard/$', views.proyek_dashboard,
    	{'template_name':'tatakelola/proyek_dashboard_diskominfo.html'}, 'proyek_dashboard'),
    url(r'^kebijakan_dashboard/$', views.kebijakan_dashboard, 
    	{'template_name' : 'tatakelola/kebijakan_dashboard_diskominfo.html'}, 
    	'kebijakan_dashboard'),
    url(r'^kebijakan/$', views.kebijakan, 
    	{'template_name': 'tatakelola/kebijakanform.html'}, 'kebijakan'),
    url(r'^evaluasiMonitoring_dashboard/$', views.emonitor, 
    	{'template_name' : 'tatakelola/em_dashboard_diskominfo.html'}, 'evaluasiMonitoring_dashboard'),
    url(r'^evaluasipertahun/(?P<id>\d+)/$', views.emonitorperTahun, 
    	{'template_name' : 'tatakelola/evaluasipertahun_diskominfo.html'}, 'evaluasipertahun'),
    url(r'^monitoring/(?P<id>\d+)/$', views.emonitor_, 
    	{'template_name': 'tatakelola/monitor_diskominfo.html'}, 'monitoring'),
    url(r'^bantuan/$', views.section, {}, 'bantuan'),
]