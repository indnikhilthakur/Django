from django.db import models
import uuid
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class new_model(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name= models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    emp_password = models.CharField(max_length = 100)


    def __str__(self) -> str:
        return self.first_name

city_choices = (
    ("one", "pune"),
    ("two", "mumbai"),
    ("three", "goa"),
    ("four", "vengurla")
)        

class model_practice(models.Model):
    boolean_only = models.BooleanField(default=True, verbose_name="boolean field")
    boolean_multi = models.BooleanField()
    char_field = models.CharField(max_length= 100, unique= True, verbose_name="character field", help_text="help text")
    date_field = models.DateField(default=timezone.now)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    email_field = models.EmailField(max_length=100)
    file_field = models.FileField(upload_to='uploads', blank=True)
    image_field = models.ImageField(upload_to='uploads', blank=True)
    integer_field = models.IntegerField()
    slug_field = models.SlugField(default=True)
    text_field = models.TextField()
    url_field = models.URLField(max_length=100)
    uuid1 = models.UUIDField(default=uuid.uuid4)
    uuid2 = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    date_and_time = models.DateTimeField()
    choice_field = models.CharField(max_length=10, choices=city_choices)
 

def save(self):
    self.slug_field = slugify(self.text_field[:30])