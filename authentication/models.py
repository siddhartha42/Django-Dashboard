# authentication/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

def user_profile_image_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/profile/<filename>
    return f'user_{instance.id}/profile/{filename}'

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=255, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    profile_image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)

    # Add other fields as needed

    # Specify related_name for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set',  # Specify related_name here
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set',  # Specify related_name here
        help_text=_('Specific permissions for this user.'),
    )

    def __str__(self):
        return self.username
