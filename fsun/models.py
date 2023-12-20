from django.db import models

# Create your models here.

# class Project(models.Model):
    # name = models.CharField(max_length=200, null=True)

    # def __str__(self) -> str:
    #     return f'{self.name}'


# class Role(models.Model):
    # name = models.CharField(max_length=200, null=True)

    # def __str__(self) -> str:
    #    return f'{self.name}'


class FieldStaffInformation(models.Model):
    fsun_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    project = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} + {self.fsun_code}'
    
    class Meta:
        ordering = ['-created']


