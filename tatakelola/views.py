from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import KebijakanForm, MonitorForm, Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, UserForm
from .models import QuestionAnswer, Section, Kebijakan, Proyek, UserProfile, EvaluasidanMonitor


@login_required
def kebijakan_dashboard(request, template_name):
	kebijakan = Kebijakan.objects.all()
	paginator = Paginator(kebijakan, 2) # Show 2 contacts per page
	page = request.GET.get('page')
	try:
		kebijakan = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		kebijakan = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		kebijakan = paginator.page(paginator.num_pages)
	context = {'kebijakan': kebijakan}
	return render(request, template_name, context)

def lihat_kebijakan(request, template_name, id):
    kebijakan = get_object_or_404(Kebijakan, id=id)
    form = KebijakanForm(instance=kebijakan)
    if request.method=="POST":
    	form = KebijakanForm(request.POST,request.FILES, instance=kebijakan)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect(reverse('tatakelola:kebijakan_dashboard'))
    # kominfo bsa ngedit
    if not request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    context = {'form': form}
    return render(request, template_name, context)

@login_required
def proyek_dashboard(request, template_name):
	proyek = Proyek.objects.all()
	paginator = Paginator(proyek, 2) # Show 2 contacts per page
	page = request.GET.get('page')
	try:
		proyek = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		proyek = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		proyek = paginator.page(paginator.num_pages)
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


@login_required
def step1(request, template_name):
    form = Step1Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

@login_required
def step2(request, template_name):
    form = Step2Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

@login_required
def step3(request, template_name):
    form = Step3Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

@login_required
def step4(request, template_name):
    form = Step4Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

@login_required
def step5(request, template_name):
    form = Step5Form()
    context = {'form': form}
    if request.user.is_staff:
    	for name, field in form.fields.items():
    		field.disabled = True
    return render(request, template_name, context)

@login_required
def kebijakan(request, template_name):
	if request.method=="POST":
		form = KebijakanForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('tatakelola:kebijakan_dashboard'))
	else:
		form = KebijakanForm()

	context = {'form': form}
	return render(request, template_name, context)


@login_required
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

@login_required
def home(request, template_name):
	context = {}
	return render(request, template_name, context)

def permission_denied(request):
	return render (request, 'registration/403.html', {})

def bad_request(request):
	return render (request, 'registration/400.html', {})

def page_not_found(request):
	return render (request, 'registration/404.html', {})

def server_error():
	return render (request, 'registration/500.html', {})