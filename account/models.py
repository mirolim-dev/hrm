from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError(_('Telefon raqam kiritilishi shart'))
        phone = phone
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create(phone, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'User'
        # abstract = True

    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=25, blank=True, verbose_name=_("Ism"))
    last_name = models.CharField(max_length=255, blank=True, verbose_name=_("Familya"))
    address = models.CharField(max_length=255, blank=True, verbose_name=_("Manzil"))
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Telefon raqam quyidagi formatda kiririlishi shart: '+9989999999'. 15 ta raqamdan ziyodini qo'llab quvvatlaydi.")
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True, verbose_name=_("Telefon raqami"))
    email = models.EmailField(unique=True, blank=True, null=True)
    GENDER_CHOICES = (
        (0, _("Ayol")),
        (1, _("Erkak"))
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name=_("Jinsi"))

    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("O'zgartirilgan vaqti"))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Qo'shilgan vaqti"))
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',  # Add related_name to avoid clash
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Add related_name to avoid clash
    )
    objects = CustomUserManager()    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']  

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.phone
        super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return super().has_perm(perm, obj)
    
    def has_module_perms(self, app_label):
        return super().has_module_perms(app_label)
    
    def __str__(self):
        return self.get_full_name()

    def display_gender(self):
        return self.GENDER_CHOICES[self.gender][1]
    