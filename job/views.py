from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job
from .forms import ApplyForm

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 1)
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
    context = {'job_detail': job_detail, 'form': form}
    return render(request, 'job/job_detail.html', context)



