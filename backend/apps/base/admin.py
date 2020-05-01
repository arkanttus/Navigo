from django.contrib import admin
from apps.base.models import Institution, TypeInstitution


class TypeInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', )


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'get_institution_others')


admin.site.register(TypeInstitution, TypeInstitutionAdmin)
admin.site.register(Institution, InstitutionAdmin)





