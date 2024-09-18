from django.contrib import admin
from django.utils import timezone
from .models import Categoria, Producto, Cliente
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import DateFieldListFilter

# Registro de modelos básicos
admin.site.register(Categoria)
admin.site.register(Producto)

# Recurso para importar/exportar clientes
class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    resource_class = ClienteResource
    list_display = (
        'nombres',
        'apellidos',
        'dni',
        'telefono',
        'email',
        'fecha_nacimiento',
        'fecha_publicacion',
        'edad',
    )
    search_fields = ('nombres', 'apellidos', 'dni', 'email')  # Filtrado por nombre y DNI
    
    actions = ['actualizar_fecha_publicacion', 'eliminar_clientes', 'enviar_correo']
    ordering = ('apellidos', 'nombres')
    list_per_page = 20
    fields = ('nombres', 'apellidos', 'dni', 'telefono', 'email', 'direccion', 'fecha_nacimiento')  # Excluye 'fecha_publicacion'

    def edad(self, obj):
        """Calcula y devuelve la edad del cliente."""
        from datetime import date
        return date.today().year - obj.fecha_nacimiento.year

    edad.short_description = 'Edad'

    def save_model(self, request, obj, form, change):
        """Establece la fecha de publicación automáticamente al guardar."""
        if not change:  # Solo se establece en la creación
            obj.fecha_publicacion = timezone.now()
        super().save_model(request, obj, form, change)

    def actualizar_fecha_publicacion(self, request, queryset):
        """Actualiza la fecha de publicación para los clientes seleccionados."""
        for cliente in queryset:
            cliente.fecha_publicacion = timezone.now()
            cliente.save()
        self.message_user(request, "Fecha de publicación actualizada para los clientes seleccionados.")

    actualizar_fecha_publicacion.short_description = "Actualizar fecha de publicación de clientes seleccionados"

   

   