from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    document = models.FileField(
        upload_to="document",
        verbose_name="Документ"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Документы"
        verbose_name_plural = "Документ"