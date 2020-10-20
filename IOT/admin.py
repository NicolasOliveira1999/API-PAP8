from django.contrib import admin
from IOT.models import Lamp,Usuario,Hist
# Register your models here.

class Lamps(admin.ModelAdmin):
    list_display=('nome','pino')
    list_display_links=('nome','pino')
    list_display_search=('nome','pino')

admin.site.register(Lamp, Lamps)

class Usuarios(admin.ModelAdmin):
    list_display=('nome','ra','senha','situacao','admin_acess')
    list_display_links=('nome','ra','senha','situacao','admin_acess')
    list_display_search=('nome','ra','situacao','admin_acess')

admin.site.register(Usuario, Usuarios)

class Hists(admin.ModelAdmin):
    list_display=('id_hist','logindate','id_usuario')
    list_display_links=('logindate','id_usuario')
    list_display_search=('logindate','id_usuario')
    
admin.site.register(Hist, Hists)



