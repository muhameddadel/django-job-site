from django.db import models

# Create your models here.
JOB_TYPE = [
    ('FT', 'Full Time'),
    ('PT', 'Part Time'),
    ('RM', 'Remote')
]

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location = 
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete= models.CASCADE)
    experience = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name