from django.db import models

# Create your models here.
class Employee(models.Model):
    gen = (
        ('Male','male'),
        ('Femail','female'),
        ('Other','other'),
    )
    departments = (
        ('administration','Administration'),
        ('system_administration','System_Administration'),
        ('application_developer','Application_Developer'),
        ('security_administration','Security_Administration'),
        ('database_administration','Database_Administration'),
        ('web_developer','Web_Developer'),
        ('helpdesk_supporter','Helpdesk_Supporter'),
        ('technical_supporter','Technical_Supporter'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,primary_key=True)          #unique=True
    contact = models.BigIntegerField(max_length=10)
    dept = models.CharField(max_length=50,choices=departments)
    gender = models.CharField(max_length=50,choices=gen,default='male')
    salary = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    image = models.ImageField(upload_to='images',null=True)

