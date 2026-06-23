from django.contrib import admin
# from store.models.tag import ProductTag
from .models import Category, Product, ProductTag, Tag, Attribute, AttributeValue, ProductAttribute
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
    def image_preview(self, obj):
        return format_html(
                '<img src="{}" style="width: 80px; height: 80px; object-fit: cover">', 
                obj.image_url)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)     
    
     

class ProductTagInline(admin.TabularInline):
    model = ProductTag
    extra = 1
    autocomplete_fields = ('tag', )
    

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1
    autocomplete_fields = ('attribute_value',)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'value']
    list_filter = ['attribute']
    search_fields = ['value', 'attribute__name']




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'name', 'price', 'category', 'stock', 'is_available', 'total_price']
    list_editable = ['price', 'stock', 'is_available']
    search_fields = ['name', 'category__name']
    list_filter = ['category', 'is_available']
    ordering = ['-created_at']
    prepopulated_fields = {'slug': ('name',)}
    
    inlines = [ProductTagInline, ProductAttributeInline]
    
    def image_preview(self, obj):
        return format_html(
                '<img src="{}" style="width: 80px; height: 80px; object-fit: cover">', 
                obj.image_url)