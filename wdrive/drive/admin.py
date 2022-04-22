from ast import Return
from django.contrib import admin
from .models import * 
from django.contrib.auth.models import User, Group

class FileAdmin(admin.ModelAdmin):
    list_display = ['filename', 'file', 'share_WWS', 'created_by', 'updated', 'created']
    search_fields = ['filename']
    list_filter = [
        'created', 'updated', 'created_by', 'share_MSM', 'share_MDC', 'share_MDN', 'share_MHF', 'share_WWA', 'share_SGS', 'share_SGE', 'share_NWA', 'share_WWM', 'share_AYS', 'share_MGS', 'share_MGN', 'share_MDS', 'share_SHS', 'share_NPT', 'share_YGW', 'share_YGS', 'share_BGW', 'share_YGN', 'share_YGE', 'share_BGE', 'share_MNS', 'share_TNY', 'share_WEC', 'share_WWS', 'share_WWT', 'share_WWH', 'share_WHH'
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.groups.filter(name='WWS').exists():
            qs_share = qs.filter(share_WWS=True)        
            qs_own = qs.filter(created_by=request.user)
            return qs_share | qs_own
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(File, FileAdmin)