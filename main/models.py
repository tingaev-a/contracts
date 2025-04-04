from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


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
    """
    Типы контрактов
    """
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

class Organization(models.Model):
    """
    Организации
    """
    name = models.CharField(max_length=200, verbose_name="Название")
    inn = models.CharField(max_length=12, verbose_name="ИНН")
    kpp = models.CharField(max_length=9, verbose_name="КПП")

    def __str__(self):
        return self.name

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
    contract_type = models.ForeignKey(
        ContractType,
        on_delete=models.CASCADE,
        related_name='contracts',
        verbose_name="Тип контракта",
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

