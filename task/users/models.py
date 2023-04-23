from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Создаем модель Пользователя унаследовав от модели AbstractUser"""
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'