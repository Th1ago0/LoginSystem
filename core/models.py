from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomManager(BaseUserManager):

	def create_user(self,email,password=None, **other_fields):

		if not email:
			raise ValueError(_('Email must be set'))
		email = self.normalize_email(email)
		user = self.model(email = email, **other_fields)
		user.password = make_password(password )
		user.save(using = self._db)
		return user


	def create_superuser(self, email, password = None, **other_fields):

		other_fields.setdefault('is_active', True)
		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser',True)

		if other_fields.get('is_staff') is not True:
			raise ValueError(_('is_staff field must be True'))
		if other_fields.get('is_superuser') is not True:
			raise ValueError(_('is_superuser field must be True'))

		return self.create_user(email,password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique = True)
	name = models.CharField(max_length = 50)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	date_joined = models.DateTimeField(default = timezone.now)

	objects = CustomManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def __str__(self):
		return self.email