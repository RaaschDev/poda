from django.contrib import admin
from .models import Service, ServiceImage, ServiceDepoiment
# Register your models here.


class ServiceImageAdmin(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceDepoimentAdmin(admin.TabularInline):
    model = ServiceDepoiment
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial_page')
    inlines = [ServiceImageAdmin, ServiceDepoimentAdmin]
