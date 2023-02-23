from .serializers import JobSerializer
from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view 

@api_view(['GET'])
def job_list_api(request):
    job_list = Job.objects.all()
    serializer = JobSerializer(job_list, many = True)

    return Response(serializer.data)


@api_view(['GET'])
def job_list_api_pk(request, pk):
    job_list_pk = Job.objects.get(pk= pk)
    serializer = JobSerializer(job_list_pk)

    return Response(serializer.data)
