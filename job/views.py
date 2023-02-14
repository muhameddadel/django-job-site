from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
from .form import ApplyForm , JobForm

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'job_list': page_obj, 'jobs': job_list }
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = Job.objects.get(slug = slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form =form.save(commit=False)
            my_form.job = job_detail
            my_form.save()

    else:
        form = ApplyForm()
    context = {'job_detail': job_detail, 'form1': form}
    return render(request, 'job/job_detail.html', context)


def add_job(request):
    
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    return render(request, 'job/add_job.html', {'form': form})
