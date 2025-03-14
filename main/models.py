from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    """
    Модель пользователя
    """
    # Дополнительные поля, если они нужны

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_user_set',  # Измените это имя на то, что вам удобно
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_user_set',  # Измените это имя на то, что вам удобно
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class ContractType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название типа договора")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.name

class Organization(models.Model):
    """
    Организации
    """
    name = models.CharField(max_length=200, verbose_name="Название")
    inn = models.CharField(max_length=12, verbose_name="ИНН")
    def __str__(self):
        return self.name

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'inn']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название организации'}),
            'inn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ИНН', 'maxlength': '12'}),
        }

        labels = {
            'name': 'Название организации',
            'inn': 'ИНН',
        }

        help_texts = {
            'name': 'Укажите полное наименование организации',
            'inn': 'Введите ИНН организации (12 цифр)',
        }

        error_messages = {
            'name': {
                'required': 'Пожалуйста, укажите название организации',
                'max_length': 'Название не должно превышать 200 символов'
            },
            'inn': {
                'required': 'Пожалуйста, укажите ИНН',
                'max_length': 'ИНН должен содержать ровно 12 цифр',
                'min_length': 'ИНН должен содержать ровно 12 цифр'
            }
        }

    def clean_inn(self):
        inn = self.cleaned_data['inn']
        if not inn.isdigit():
            raise forms.ValidationError("ИНН должен содержать только цифры")
        if len(inn) != 12:
            raise forms.ValidationError("ИНН должен содержать ровно 12 цифр")
        return inn


class Position(models.Model):
    """
    Должности
    """
    name = models.CharField(max_length=100, verbose_name="Название")
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='positions',
        verbose_name="Организация"
    )

    def __str__(self):
        return self.name

class Contract(models.Model):
    """
    Контракты
    """
    number = models.CharField(max_length=50, verbose_name="Номер")
    date_start = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(verbose_name="Дата окончания")
    contract_type = models.CharField(
        ContractType,
        max_length=100,
        default='Доходный договор'  # Замените на подходящее значение
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='contracts',
        verbose_name="Организация"
    )

    def __str__(self):
        return f"Контракт {self.number}"

class File(models.Model):
    """
    Файлы
    """
    file = models.FileField(upload_to='files/', verbose_name="Файл")
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='files',
        verbose_name="Контракт"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Загружено")

    def __str__(self):
        return self.file.name


class Meta:
    verbose_name = "Организация"
    verbose_name_plural = "Организации"
    ordering = ['-registration_date']
    def __str__(self):
        return self.verbose_namename
