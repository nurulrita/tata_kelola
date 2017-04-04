from django.contrib import admin
from .models import QuestionAnswer, Step1, Step2, Step3, Step4, Step5, Section
    
admin.site.register(Step1)
admin.site.register(Step2)
admin.site.register(Step3)
admin.site.register(Step4)
admin.site.register(Step5)
admin.site.register(QuestionAnswer)
admin.site.register(Section)