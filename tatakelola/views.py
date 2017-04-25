from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import KebijakanForm, MonitorForm, Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, UserForm
from .models import QuestionAnswer, Section, Kebijakan, Proyek, UserProfile, EvaluasidanMonitor


@login_required
def kebijakan_dashboard(request, template_name):
	kebijakan = Kebijakan.objects.all()
	context = {'kebijakan': kebijakan}
	return render(request, template_name, context)

def lihat_kebijakan(request, template_name, id):
    kebijakan = Kebijakan.objects.get(id=id)
    form = KebijakanForm(instance=kebijakan)
    for name, field in form.fields.items():
    	field.disabled = True
    context = {'form': form}
    return render(request, template_name, context)

@login_required
def proyek_dashboard(request, template_name):
	proyek = Proyek.objects.all()
	context = {'proyek' : proyek}
	return render(request, template_name, context)

@login_required
def user_dashboard(request, template_name):
    userprofile = UserProfile.objects.all()
    context = {'userprofile': userprofile}
    return render(request, template_name, context)

@login_required
def emonitor(request, template_name):
    emonitor = EvaluasidanMonitor.objects.all()
    context = {'emonitor': emonitor}
    return render(request, template_name, context)

@login_required
def emonitorperTahun(request, template_name, id):
    emonitor = EvaluasidanMonitor.objects.filter(proyek__id=id)
    context = {'emonitor': emonitor}
    return render(request, template_name, context)

@login_required
def emonitor_(request, template_name, id):
    emonitor = EvaluasidanMonitor.objects.get(id=id)
    form = MonitorForm(instance=emonitor)
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)


def step1(request, template_name):
    form = Step1Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

def step2(request, template_name):
    form = Step2Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

def step3(request, template_name):
    form = Step3Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

def step4(request, template_name):
    form = Step4Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

def step5(request, template_name):
    form = Step5Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

def kebijakan(request, template_name):
    form = KebijakanForm()
    context = {'form': form}
    return render(request, template_name, context)


def user(request, template_name):
    form = UserForm()
    context = {'form': form}
    return render(request, template_name, context)

@login_required
def section(request):

    context_dict = {}

    try:
        section = Section.objects.order_by('name')
        faq = QuestionAnswer.objects.all()
        # Adds our results list to the template context under name pages.
        context_dict['faq'] = faq
        context_dict['section'] = section
    except Section.DoesNotExist:
        pass


    return render(request, 'tatakelola/bantuan.html', context_dict)

@login_required
def notifications(request, template_name):
    notifs = request.user.notifications.unread()
    context = {'notifs': notifs}
    return render(request, template_name, context)
    

@login_required
def notifications_mark_all_as_read(request): 
    request.user.notifications.mark_all_as_read()
    return redirect('/comment_filter/notifications/')
   