from django.contrib import admin
from .models import Svcs, Indl, Country, GovtOrder, Course, CourseOffer, CourseAcceptance, Visit, YearlyState, Sections

@admin.register(Svcs)
class SvcsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Indl)
class IndlAdmin(admin.ModelAdmin):
    list_display = ('Service_Number', 'Rank', 'name',)
    search_fields = ('Service_Number', 'Rank', 'name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(GovtOrder)
class GovtOrderAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'svcs', 'start_date', 'end_date')  # Fixed the list_display values
    search_fields = ('event_name', 'svcs__name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'institute_name', 'start_date', 'end_date', 'country', 'course_duration',)
    search_fields = ('name', 'country__name',)

@admin.register(CourseOffer)
class CourseOfferAdmin(admin.ModelAdmin):
    list_display = ('svcs', 'country', 'course',)
    search_fields = ('svcs__name', 'country__name', 'course__name',)

@admin.register(CourseAcceptance)
class CourseAcceptanceAdmin(admin.ModelAdmin):
    list_display = ('country', 'course',)
    search_fields = ('country__name', 'course__name',)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('svcs', 'country',)
    search_fields = ('svcs__name', 'country__name',)

@admin.register(YearlyState)
class YearlyStateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sections)