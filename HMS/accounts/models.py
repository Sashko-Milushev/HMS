from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import validators
from enum import Enum

from django.db import models

from HMS.accounts.managers import AppUserManager
from HMS.accounts.model_mixins import ChoicesEnumMixin


class Position(ChoicesEnumMixin, Enum):
    receptionist = 'Receptionist'
    front_office_manager = 'Front office manager'
    hotel_manager = 'Hotel manager'


class Employee(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 30
    USERNAME_MIN_LEN = 2

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(NAME_MIN_LEN),),
        blank=False,
        null=False
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(NAME_MIN_LEN),),
        blank=False,
        null=False
    )

    username = models.CharField(
        verbose_name='Username',
        max_length=USERNAME_MAX_LEN,
        unique=True,
        help_text=(
            "Required. 30 characters or fewer. Letters and digits only."
        ),
        validators=(username_validator, validators.MinLengthValidator(USERNAME_MIN_LEN),),
        blank=False,
        null=False
    )
    position = models.CharField(
        choices=Position.choices(),
        max_length=Position.max_len(),
        blank=False,
        null=False
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        validators=(validators.EmailValidator(message='Invalid Email'),),
        blank=False,
        null=False
    )
    date_joined = models.DateField(
        blank=True,
        null=True
    )

    is_staff = models.BooleanField(
        default=True,
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(
        default=True,
        blank=False,
        null=False,
    )

    USERNAME_FIELD = 'username'
    objects = AppUserManager()
