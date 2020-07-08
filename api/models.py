from django.db import models

# Create your models here.
class Computer(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    brand=models.CharField(max_length=20)

    class Meta:
        db_table='api_comp'
        verbose_name='电脑'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name