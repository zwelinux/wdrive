from ast import Return
from django.contrib import admin
from .models import * 
from django.contrib.auth.models import User, Group

class FileAdmin(admin.ModelAdmin):
    list_display = ['filename', 'file', 'share_MGS', 'created_by', 'updated', 'created']
    search_fields = ['filename']
    list_filter = [
        'created', 'updated', 'created_by', 'share_MSM', 'share_MDC', 'share_MDN', 'share_MHF', 'share_WWA', 'share_SGS', 'share_SGE', 'share_NWA', 'share_WWM', 'share_AYS', 'share_MGS', 'share_MGN', 'share_MDS', 'share_SHS', 'share_NPT', 'share_YGW', 'share_YGS', 'share_BGW', 'share_YGN', 'share_YGE', 'share_BGE', 'share_MNS', 'share_TNY', 'share_WEC', 'share_WWS', 'share_WWT', 'share_WWH', 'share_WHH'
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # elif request.user.groups.filter(name='AYS').exists():
        #     qs_share = qs.filter(share_AYS=True)        
        #     qs_own = qs.filter(created_by=request.user)
        #     return qs_share | qs_own
        elif request.user.groups.filter(name='AYS').exists():
            qs_share = qs.filter(share_AYS=True)
            return qs_share
        elif request.user.groups.filter(name='BGE').exists():
            qs_share = qs.filter(share_BGE=True)
            return qs_share
        elif request.user.groups.filter(name='BGW').exists():
            qs_share = qs.filter(share_BGW=True)
            return qs_share
        elif request.user.groups.filter(name='MDC').exists():
            qs_share = qs.filter(share_MDC=True)
            return qs_share
        elif request.user.groups.filter(name='MDN').exists():
            qs_share = qs.filter(share_MDN=True)
            return qs_share
        elif request.user.groups.filter(name='MDS').exists():
            qs_share = qs.filter(share_MDS=True)
            return qs_share
        elif request.user.groups.filter(name='MGN').exists():
            qs_share = qs.filter(share_MGN=True)
            return qs_share
        elif request.user.groups.filter(name='MGS').exists():
            qs_share = qs.filter(share_MGS=True)
            qs_own = qs.filter(created_by=request.user)
            return qs_share | qs_own
        elif request.user.groups.filter(name='MHF').exists():
            qs_share = qs.filter(share_MHF=True)
            return qs_share
        elif request.user.groups.filter(name='MNS').exists():
            qs_share = qs.filter(share_MNS=True)
            return qs_share
        elif request.user.groups.filter(name='MSM').exists():
            qs_share = qs.filter(share_MSM=True)
            return qs_share
        elif request.user.groups.filter(name='NPT').exists():
            qs_share = qs.filter(share_NPT=True)
            return qs_share
        elif request.user.groups.filter(name='NWA').exists():
            qs_share = qs.filter(share_NWA=True)
            return qs_share
        elif request.user.groups.filter(name='SGE').exists():
            qs_share = qs.filter(share_SGE=True)
            return qs_share
        elif request.user.groups.filter(name='SGS').exists():
            qs_share = qs.filter(share_SGS=True)
            return qs_share
        elif request.user.groups.filter(name='SHS').exists():
            qs_share = qs.filter(share_SHS=True)
            return qs_share
        elif request.user.groups.filter(name='TNY').exists():
            qs_share = qs.filter(share_TNY=True)
            return qs_share
        elif request.user.groups.filter(name='WEC').exists():
            qs_share = qs.filter(share_WEC=True)
            return qs_share
        elif request.user.groups.filter(name='WHH').exists():
            qs_share = qs.filter(share_WHH=True)
            return qs_share
        elif request.user.groups.filter(name='WWA').exists():
            qs_share = qs.filter(share_WWA=True)
            return qs_share
        elif request.user.groups.filter(name='WWH').exists():
            qs_share = qs.filter(share_WWH=True)
            return qs_share
        elif request.user.groups.filter(name='WWM').exists():
            qs_share = qs.filter(share_WWM=True)
            return qs_share
        elif request.user.groups.filter(name='WWS').exists():
            qs_share = qs.filter(share_WWS=True)
            return qs_share
        elif request.user.groups.filter(name='WWT').exists():
            qs_share = qs.filter(share_WWT=True)
            return qs_share
        elif request.user.groups.filter(name='YGE').exists():
            qs_share = qs.filter(share_YGE=True)
            return qs_share
        elif request.user.groups.filter(name='YGN').exists():
            qs_share = qs.filter(share_YGN=True)
            return qs_share
        elif request.user.groups.filter(name='YGS').exists():
            qs_share = qs.filter(share_YGS=True)
            return qs_share
        elif request.user.groups.filter(name='YGW').exists():
            qs_share = qs.filter(share_YGW=True)
            return qs_share
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(File, FileAdmin)