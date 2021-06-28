from django.contrib import admin
from .models import AppCategory, App

# Create custom views, define what editable and calculated fields for models in Admin module and 

class AppAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "app_name",
        "release_date",
        "app_image",
        "app_category",
        )
    
    
    # # Calculated fields displayed in list view in Admin module
    # def order_val(self, obj: Execution) -> str:
    #     return f"{(obj.quantity * obj.price):.2f}"
    
    
    # Fields that can be edited in the list view in Admin module
    list_editable = (
        
        )
    

class AppCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "category_name",
        )
    
    # # Calculated fields displayed in list view in Admin module
    # def order_val(self, obj: Execution) -> str:
    #     return f"{(obj.quantity * obj.price):.2f}"
    
    
    # Fields that can be edited in the list view in Admin module
    list_editable = (
        
        )



# Register your models here.

admin.site.register(
    AppCategory,
    AppCategoryAdmin,
    )

admin.site.register(
    App,
    AppAdmin,
    )