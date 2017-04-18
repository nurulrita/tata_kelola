from django.contrib import admin
from .models import EvaluasidanMonitor, Kebijakan, Proyek, QuestionAnswer, Step1, Step2, Step3, Step4, Step5, Section, UserProfile

class EvaluasidanMonitorAdmin(admin.ModelAdmin):
    list_display = ('opd', 'proyek', 'tahun')

class KebijakanAdmin(admin.ModelAdmin):
    list_display = ('no_perwal', 'nama_perwal','proyek', 'file')

class ProyekAdmin(admin.ModelAdmin):
    list_display = ('nama_proyek', 'latest_step','opd', 'status')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id_pegawai', 'NIP','nama', 'jenis_user')


admin.site.register(EvaluasidanMonitor, EvaluasidanMonitorAdmin)
admin.site.register(Kebijakan, KebijakanAdmin)
admin.site.register(Proyek, ProyekAdmin)
admin.site.register(Step1)
admin.site.register(Step2)
admin.site.register(Step3)
admin.site.register(Step4)
admin.site.register(Step5)
admin.site.register(QuestionAnswer)
admin.site.register(Section)
admin.site.register(UserProfile, UserProfileAdmin)