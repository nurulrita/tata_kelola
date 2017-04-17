from django.contrib import admin
from .models import Kebijakan, QuestionAnswer, Step1, Step2, Step3, Step4, Step5, Section, UserProfile
    
admin.site.register(Kebijakan)
admin.site.register(Step1)
admin.site.register(Step2)
admin.site.register(Step3)
admin.site.register(Step4)
admin.site.register(Step5)
admin.site.register(QuestionAnswer)
admin.site.register(Section)
admin.site.register(UserProfile)