from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password = None, is_admin = False):
        if not email:
            raise ValueError("Email cannot be empty")
        if not password:
            raise ValueError("Password cannot be empty")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.save(using = self._db)
        return user_obj
    
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        # user.staff = True

        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email =  models.EmailField(unique= True, max_length= 255)
    admin = models.BooleanField(default= False)
    staff = models.BooleanField(default= False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    user = UserManager()
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_staff(self):
        return self.staff