from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StudentApplication)
admin.site.register(TouristInquiry)

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slide_type', 'is_active', 'updated_at']
    list_filter = ['slide_type', 'is_active', 'created_at']
    search_fields = ['title', 'alt_text']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slide_type', 'image', 'alt_text')
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class StudentDestinationImageInline(admin.TabularInline):
    model = StudentDestinationImage
    extra = 1

@admin.register(StudentDestination)
class StudentDestinationAdmin(admin.ModelAdmin):
    inlines = [StudentDestinationImageInline]


class AttractionSiteImageInline(admin.TabularInline):
    model = AttractionSiteImage
    extra = 1


@admin.register(AttractionSite)
class AttractionSiteAdmin(admin.ModelAdmin):
    inlines = [AttractionSiteImageInline]
    list_display = ["name", "destination", "created_at"]
    search_fields = ["name", "destination__name"]


class TouristDestinationImageInline(admin.TabularInline):
    model = TouristDestinationImage
    extra = 1


class AttractionInline(admin.TabularInline):
    model = AttractionSite
    extra = 1


@admin.register(TouristDestination)
class TouristDestinationAdmin(admin.ModelAdmin):
    inlines = [TouristDestinationImageInline, AttractionInline]
    list_display = ["name"]
    search_fields = ["name"]

