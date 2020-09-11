from django.contrib import admin
from myapp import models
# Register your models here.
class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)
    search_fields=('topic_name',)
    list_filter=('topic_name',)
class WebpageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('topic','name','url')
    list_editable=('name',)
    list_filter=('topic',)
class AccessDetailsAdminView(admin.ModelAdmin):
    list_display=('webpage','datetime')
    list_display_links=('webpage',)
    search_fields=('webpage','datetime')
    list_filter=('webpage',)
admin.site.register(models.Topic,TopicAdminView)
admin.site.register(models.Webpage,WebpageAdminView)
admin.site.register(models.AccessDetails,AccessDetailsAdminView)
