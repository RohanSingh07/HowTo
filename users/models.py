from django.db import models
# Auth models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager

# Account Manager
class MyAccountManager(BaseUserManager):

    # what happens when a user and superuser is created
    def create_user(self,username,password=None): # add the fields which are required for user

        user = self.model(
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password):
        user = self.create_user(
            username=username,
            password=password

        )

        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

# User model
class Account(AbstractBaseUser):

    # username
    username = models.CharField(verbose_name='username',max_length=50,unique=True)
    # Can choose to have email
    email=models.EmailField(blank=True,null=True,unique=True)
    # Signed Up date
    date_joined = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_joined',auto_now_add=True)

    # Active or deactivated account
    is_active = models.BooleanField(default=True)
    # Can access the admin panel or not
    is_staff = models.BooleanField(default=False)
    # Superuser status
    is_superuser = models.BooleanField(default=False)
    # whatever you want to login with
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    # tell Account where is Account manager located
    objects = MyAccountManager()

    # what will be printed when we will refer to this user object
    def __str__(self):
        return str(self.username)
    # required functions

    def has_perm(self,perm,obj=None): # what permission would this type of user have
        return self.is_superuser

    def has_module_perms(self,app_label):
        return True








