from django.contrib import admin
from .models import Hospital_Type, Hospital, Contact

# Register your models here.

#admin.site.register(Hospital_Type, Hospital)

@admin.register(Hospital_Type)
class Hospital_TypeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('type_name',)}
	list_display = ['type_name', 'slug']
	list_filter = ['type_name', 'slug']

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ['category', 'name', 'address', 'logo']
	list_filter = ['category', 'address']

admin.site.register(Contact)
