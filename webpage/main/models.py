from django.db import models

# Create your models here.

class MainPage(models.Model):
    page_title = models.CharField(max_length=200)
    wallet_address = models.TextField()
    last_update = models.DateTimeField("Última Atualização")

    def __str__(self):
        return self.page_title


