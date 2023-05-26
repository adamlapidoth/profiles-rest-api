from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserProfileManager(BaseUserManager):
    """ Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """
        Create a mew user profile
        :param email: An email address
        :param name: Name of user
        :param password: User password
        :return: A user
        """
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a new superuser with given details
        :param email: An email address
        :param name: Name of user
        :param password: User password
        :return: A superuser
        """
        user = self.create_user(email=email, name=name, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve full name of user
        :return: Full name of user
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve short name of user
        :return: Short name of user
        """
        return self.name

    def __str__(self):
        """
        Return string representation of our user
        :return: The string representation of the user
        """
        return self.email
