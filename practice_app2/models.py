from django.db import models
# from django.utils import timezone
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField


city_choices = (
    ("one", "pune"),
    ("two", "mumbai"),
    ("three", "goa"),
    ("four", "vengurla")
)


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



class model_practice4(models.Model):
    name_char_field3 = models.CharField(max_length=100)
    image_field = models.ImageField(null=True, blank=True, upload_to='images/')
    file_field = models.FileField(null = True, blank = True, upload_to='files/')

    def __str__(self) -> str:
        return self.name_char_field3


class model_student(models.Model):
    s_first_name = models.CharField(max_length = 100)
    s_last_name= models.CharField(max_length = 100)
    s_email = models.EmailField(max_length = 100, unique=True)
    s_emp_password = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.s_first_name


class model_sd(models.Model):
    sd_first_name = models.CharField(max_length = 100)
    sd_email = models.ForeignKey(model_student, to_field="s_email", on_delete=models.CASCADE)
    sd_branch = models.CharField(max_length=100)
    sd_age = models.IntegerField()
    sd_contact = PhoneNumberField()
    sd_city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.sd_first_name


class model_sc(models.Model):
    sc_branch = models.CharField(max_length=100)
    sc_email = models.ForeignKey(model_student, to_field="s_email", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.sc_branch

class model_movies(models.Model):
    m_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.m_name

class model_characters(models.Model):
    c_name = models.CharField(max_length=100)
    c_movie = models.ManyToManyField(model_movies)

    def __str__(self) -> str:
        return self.c_name