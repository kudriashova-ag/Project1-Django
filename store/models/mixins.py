from django.db import models
from django.conf import settings

def get_name(instance, filename):
        return f'{instance.__class__.__name__.lower()}/{filename}'

class ImageMixin(models.Model):
    image = models.ImageField('Зображення', upload_to=get_name, blank=True, null=True)
    
    @property
    def image_url(self):
        if self.image:
            return self.image.url  
        return settings.STATIC_URL + 'images/no-photo.webp' 
    
    class Meta:
        abstract = True



class SlugMixin(models.Model):
    slug = models.SlugField('URL',unique=True)  # url-сумісний рядок 
    
    class Meta:
        abstract = True
        
        

class TimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True