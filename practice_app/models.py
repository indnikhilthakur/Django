from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
city_choices = (
    ("one", "pune"),
    ("two", "mumbai"),
    ("three", "goa"),
    ("four", "vengurla")
)

class model_practice_app(models.Model):
    char_name_field = models.CharField(max_length= 100, unique= True, verbose_name="character field", help_text="help text")
    date_field = models.DateField(default=timezone.now)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    email_field = models.EmailField(max_length=100)
    boolean_only = models.BooleanField(default=True, verbose_name="boolean field")
    
    
   
   
    def __str__(self) -> str:
        return self.char_name_field

class model_practice2(models.Model):
    char_name_field2 = models.CharField(max_length= 100)
    integer_field = models.IntegerField()
    slug_field = models.SlugField(default=True)
    text_field = models.TextField()
    url_field = models.URLField(max_length=100)
    choice_field = models.CharField(max_length=10, choices=city_choices)

    

    def __str__(self) -> str:
        return self.char_name_field2

def save(self):
    self.slug_field = slugify(self.text_field[:30])