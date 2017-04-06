from django.shortcuts import render

from .forms import KebijakanForm, MonitorForm, Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, UserForm
from .models import QuestionAnswer, Section

def step1(request, template_name):
    form = Step1Form()
    context = {'form': form}
    return render(request, template_name, context)

def step2(request, template_name):
    form = Step2Form()
    context = {'form': form}
    return render(request, template_name, context)

def step3(request, template_name):
    form = Step3Form()
    context = {'form': form}
    return render(request, template_name, context)

def step4(request, template_name):
    form = Step4Form()
    context = {'form': form}
    return render(request, template_name, context)

def step5(request, template_name):
    form = Step5Form()
    context = {'form': form}
    return render(request, template_name, context)

def kebijakan(request, template_name):
    form = KebijakanForm()
    context = {'form': form}
    return render(request, template_name, context)

def monitor(request, template_name):
    form = MonitorForm()
    context = {'form': form}
    return render(request, template_name, context)

def user(request, template_name):
    form = UserForm()
    context = {'form': form}
    return render(request, template_name, context)

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

def notifications(request, template_name):
    if request.user.is_authenticated:
        notifs = request.user.notifications.unread()
        context = {'notifs': notifs}
        return render(request, template_name, context)
    else:
        return redirect('/')

def notifications_mark_all_as_read(request):
    if request.user.is_authenticated:
        request.user.notifications.mark_all_as_read()
        return redirect('/comment_filter/notifications/')
    else:
        return redirect('/')