from django import forms

from .models import EvaluasidanMonitor, Kebijakan, Proyek, Step1, Step2, Step3, Step4, Step5, User


class KebijakanForm(forms.ModelForm):
    class Meta:
        model = Kebijakan
        exclude = ('proyek',)

class ProyekForm(forms.ModelForm):
    class Meta:
        model = Proyek
        fields = ('nama_proyek',)

class Step1Form(forms.ModelForm):
    class Meta:
        model = Step1
        exclude = ('proyek',)

class Step2Form(forms.ModelForm):
    class Meta:
        model = Step2
        exclude = ('proyek',)

class Step3Form(forms.ModelForm):
    class Meta:
        model = Step3
        exclude = ('proyek',)

class Step4Form(forms.ModelForm):
    class Meta:
        model = Step4
        exclude = ('proyek',)

class Step5Form(forms.ModelForm):
    class Meta:
        model = Step5
        exclude = ('proyek',)

class MonitorForm(forms.ModelForm):
    class Meta:
        model = EvaluasidanMonitor
        exclude = ('proyek',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = '__all__'
