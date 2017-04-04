from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns =[
	url(r'^notifikasi/$', TemplateView.as_view(template_name="tatakelola/notifikasi.html"), {}, 'notifikasi'),
    url(r'^step1/$', views.step1, {'template_name': 'tatakelola/step1.html'}, 'step1'),
    url(r'^step2/$', views.step2, {'template_name': 'tatakelola/step2.html'}, 'step2'),
    url(r'^step3/$', views.step3, {'template_name': 'tatakelola/step3.html'}, 'step3'),
    url(r'^step4/$', views.step4, {'template_name': 'tatakelola/step4.html'}, 'step4'),
    url(r'^step5/$', views.step5, {'template_name': 'tatakelola/step5.html'}, 'step5'),
    url(r'^home/$', TemplateView.as_view(template_name="tatakelola/home_OPD.html"), {}, 'home'),
    url(r'^home1/$', TemplateView.as_view(template_name="tatakelola/home.html"), {}, 'home1'),
    url(r'^user_dashboard/$', views.user, {'template_name': 'tatakelola/user_dashboard.html'}, 'user_dashboard'),
    url(r'^user/$', views.user, {'template_name': 'tatakelola/userform.html'}, 'user'),
    url(r'^proyek_dashboard/$', TemplateView.as_view(template_name="tatakelola/proyek_dashboard.html"), {}, 'proyek_dashboard'),
    url(r'^proyek_dashboard1/$', TemplateView.as_view(template_name="tatakelola/proyek_dashboard_diskominfo.html"), {}, 'proyek_dashboard1'),
    url(r'^kebijakan_dashboard/$', TemplateView.as_view(template_name="tatakelola/kebijakan_dashboard_OPD.html"), {}, 'kebijakan_dashboard'),
    url(r'^kebijakan_dashboard1/$', TemplateView.as_view(template_name="tatakelola/kebijakan_dashboard_diskominfo.html"), {}, 'kebijakan_dashboard1'),
    url(r'^kebijakan/$', views.kebijakan, {'template_name': 'tatakelola/kebijakanform.html'}, 'kebijakan'),
    url(r'^evaluasiMonitoring_dashboard1/$', TemplateView.as_view(template_name="tatakelola/em_dashboard_diskominfo.html"), {}, 'evaluasiMonitoring_dashboard1'),
    url(r'^evaluasipertahun1/$', TemplateView.as_view(template_name="tatakelola/evaluasipertahun_diskominfo.html"), {}, 'evaluasipertahun1'),
    url(r'^monitoring1/$', views.monitor, {'template_name': 'tatakelola/monitor_diskominfo.html'}, 'monitoring1'),
    url(r'^bantuan/$', views.section, {}, 'bantuan'),
]