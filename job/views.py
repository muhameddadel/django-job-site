from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'job_list': page_obj}
    return render(request, 'job/job_list.html', context)

def job_detail(request, id):
    job_detail = Job.objects.get(id = id)
    context = {'job_detail': job_detail}
    return render(request, 'job/job_detail.html', context)