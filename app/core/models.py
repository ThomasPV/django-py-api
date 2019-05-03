from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,email,phone,password=None,**extra_fields):
        if not email :
           raise(ValueError('No Email Provided'))
        user = self.model(email=self.normalize_email(email),phone_number=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,email,password=None):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    email = models.EmailField( max_length=254,unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=10,default=999999999) 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

