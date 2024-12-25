from django.contrib import admin
from .models import Menu, Dish

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin panel customization for the Menu model.
    """
    list_display = ('id', 'category_name') 
    search_fields = ('category_name',) 
    ordering = ('category_name',) 

    def get_category_display(self, obj):
        return obj.get_category_name_display()
    get_category_display.short_description = 'Menu Category'

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """
    Admin panel customization for the Dish model.
    """
    list_display = ('id', 'name', 'menu', 'price', 'description_preview')
    list_filter = ('menu',)  
    search_fields = ('name', 'menu__category_name')  
    ordering = ('menu', 'name')
    list_per_page = 20

    def description_preview(self, obj):
        """
        Show a preview of the description (truncated to 50 characters).
        """
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_preview.short_description = 'Description Preview'
