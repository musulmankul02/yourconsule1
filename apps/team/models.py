from django.db import models

# Create your models here.
class AboutTeam(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "О нашей команде"
        verbose_name_plural = "О нашей команде"
        
class Team(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Профессия"
    )
    descriptions = models.TextField(
        verbose_name="Девиз"
    )
    image = models.ImageField(
        upload_to="team_image"
    )
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True,null=True
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp",
        blank=True,null=True
    )   


    def __str__(self):
        return f"{self.title} - {self.work}"
    
    class Meta:
        verbose_name = "Наши юристы"
        verbose_name_plural = "Наш юрист"
        