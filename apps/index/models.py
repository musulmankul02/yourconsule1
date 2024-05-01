from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=244,
        verbose_name="Название сайта",
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo_site"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер",
        blank=True,null=True        
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True,null=True    
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank=True,null=True        
    )
    graphic = models.CharField(
        max_length=255,
        verbose_name="График работы",
        blank=True,null=True
    )
    graphic_clock = models.CharField(
        max_length=255,
        verbose_name="График работы в часах",
        blank=True,null=True
    )
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True,null=True        
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True,null=True        
    )
    tiktok = models.URLField(
        verbose_name="Tiktok",
        blank=True,null=True        
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp",
        blank=True,null=True        
    )
    youtube = models.URLField(
        verbose_name="Youtube",
        blank=True,null=True        
    )
    app = models.URLField(
        verbose_name="Ссылка для приложения",
        blank=True,null=True        
    )
    
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        
class Slide(models.Model):
    image = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография для слайда"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название для слайда"
    )
    descriptions = models.TextField(
        verbose_name="Описание для слайда"
    )
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Слайды"
        verbose_name_plural = "Слайды"
        
class Service(models.Model):
    image = models.ImageField(
        upload_to="servie_image",
        verbose_name="Наши услуги"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название услуги"
    )
    descriptions = models.TextField(
        verbose_name="Описание про нащших услуг"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуга"
        
class Review(models.Model):
    message = models.TextField(
        verbose_name="Отзыв"
    )
    name  = models.CharField(
        max_length=255,
        verbose_name="Сообщение"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзыв"