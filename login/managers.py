from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from .messages import VALIDATION_ERR_MSG
# from login.models import User

# User = get_user_model()

class UserManager(BaseUserManager):
    """
        Custom User Manager For User.
    """
    use_in_migrations = True

    def _create_user(self, email, name, password, **extra_fields):  # mobile_number
        """
            Create and save a user with the given email and password.
        """
        if not name:
            raise ValueError(VALIDATION_ERR_MSG['FIRSTNAME_REQUIRED'])

        if not email:
            raise ValueError(VALIDATION_ERR_MSG['EMAIL_REQUIRED'])

        user = self.model(
            name=name, email=email, **extra_fields)  # mobile_number=mobile_number
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password=None, **extra_fields):  # mobile_number
        """
            Create User with Default Access
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password, **extra_fields)  # mobile_number

    def create_superuser(self, email, name, password, **extra_fields):  # mobile_number
        """
            Create User with Admin Accessibility
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, name, password, **extra_fields)  # mobile_number