from django.db import models

# Create your models here.

class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Первое описание"
    )
    desscriptions2 = models.TextField(
        verbose_name="Второе описание"
    )
    image = models.ImageField(
        upload_to="about_image",
        verbose_name="Фотография"
    )
    experience = models.CharField(
        max_length=255,
        verbose_name="опыт"
    )
    
    def  __str__(self):
        return f" {self.descriptions} - {self.desscriptions2}"
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        
class History(models.Model):
    years = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="history_image",
        verbose_name="Фотография"
    )
    
    def __str__(self):
        return f"{self.years} - {self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Наши истории"
        verbose_name_plural = "Наша история"
        
class Number(models.Model):
    clients = models.CharField(
        max_length=255,
        verbose_name="Активные клиенты"
    )
    review = models.CharField(
        max_length=255,
        verbose_name="Положительных отзывов"
    )
    team = models.CharField(
        max_length=255,
        verbose_name="Юристов"
    )
    
    def __str__(self):
        return f"{self.clients} - {self.review} - {self.team}"
    
    class Meta:
        verbose_name = "Мы в числах"
        verbose_name_plural = "Мы в числах"

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    
    def __str__(self):
        return f"{self.name} - {self.email} - {self.message} "
    
    class Meta:
        verbose_name = "Обратные связи"
        verbose_name_plural = "Обратная связь"