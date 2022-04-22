from statistics import mode
from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User, Group

def shs_file_path(instance, filename):
    created_by = str(instance.created_by)
    return '/'.join(['shs_files', created_by, instance.filename, filename])

class File(models.Model):
    filename = models.CharField(max_length=255, help_text="file အမည်")
    file = models.FileField(upload_to=shs_file_path)
    share_MSM = models.BooleanField(default=False)
    share_MDC = models.BooleanField(default=False)
    share_MDN = models.BooleanField(default=False)
    share_MHF = models.BooleanField(default=False)
    share_WWA = models.BooleanField(default=False)
    share_SGS = models.BooleanField(default=False)
    share_SGE = models.BooleanField(default=False)
    share_NWA = models.BooleanField(default=False)
    share_WWM = models.BooleanField(default=False)
    share_AYS = models.BooleanField(default=False)
    share_MGS = models.BooleanField(default=False)
    share_MGN = models.BooleanField(default=False)
    share_MDS = models.BooleanField(default=False)
    share_SHS = models.BooleanField(default=False)
    share_NPT = models.BooleanField(default=False)
    share_YGW = models.BooleanField(default=False)
    share_YGS = models.BooleanField(default=False)
    share_BGW = models.BooleanField(default=False)
    share_YGN = models.BooleanField(default=False)
    share_YGE = models.BooleanField(default=False)
    share_BGE = models.BooleanField(default=False)
    share_MNS = models.BooleanField(default=False)
    share_TNY = models.BooleanField(default=False)
    share_WEC = models.BooleanField(default=False)
    share_WWS = models.BooleanField(default=False)
    share_WWT = models.BooleanField(default=False)
    share_WWH = models.BooleanField(default=False)
    share_WHH = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE, related_name="shs")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename
