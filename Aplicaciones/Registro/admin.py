from django.contrib import admin
from .models import Registro, Oficina, RegistroOficina

# Register your models here.

class RegistroOficinaInline(admin.TabularInline):
    model = RegistroOficina
    extra = 1
    autocomplete_fields = ['idoficina']

class RegistroRFIDadmin(admin.ModelAdmin):
    inlines = [RegistroOficinaInline,]
    list_display = ('codigoRFID', 'nombre', 'apellido', 'cc',)
    list_display_links = ('codigoRFID', 'nombre',)
    search_fields = ('cc',)
    
    
class OficinaAdmin(admin.ModelAdmin):
    list_display = ('idoficina', 'oficina')
    list_display_links = ('oficina',)
    search_fields = ('oficina',)
    


admin.site.register(Registro, RegistroRFIDadmin)
admin.site.register(Oficina, OficinaAdmin)
admin.site.register(RegistroOficina)