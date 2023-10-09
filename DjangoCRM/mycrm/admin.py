from django.contrib import admin
from .models import Record
# from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display=['created_at','first_name','last_name','email','phone','city','state']