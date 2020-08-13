from django.contrib import admin
from myapp.models import Resumedata
# Register your models here.
class ResumedataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Resumedata._meta.fields if field.name != "id"]
admin.site.register(Resumedata,ResumedataAdmin)
