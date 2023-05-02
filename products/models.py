from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import uuid
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
# Create your models here.


admin_role = [
    ("SE", "Seller"),
    ("CU", "Customer")
]


class User(AbstractBaseUser,PermissionsMixin):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20,null=True,blank=True)
    last_name = models.CharField(max_length=20,null=True,blank=True)
    roles = models.CharField(max_length = 2,choices=admin_role)
    avtar = models.URLField(max_length = 200,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    zipcode = models.CharField(max_length=10,null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')




class product(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    item_name = models.CharField(max_length=100,null=True,blank=True)
    item_image = models.CharField(max_length = 200,null=True,blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)


