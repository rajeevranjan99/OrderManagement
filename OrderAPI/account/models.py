from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,name,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email Field is required")
        email = self.normalize_email(email)
        user = self.model(name=name,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name=self.name, email=email,password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default=False)
    

    objects = UserManager()


    USERNAME_FIELD= "email"
    #REQUIRED_FIELD = ["name"]
   
    def __str__(self):
        return  self.email 


