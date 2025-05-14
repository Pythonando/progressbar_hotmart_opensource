from django.db import models

# Create your models here.
class Batch(models.Model):
    batch = models.CharField(max_length=64)
    total_tickets = models.PositiveIntegerField(default=0)
    tickets_sales = models.PositiveIntegerField(default=0)
    offer_code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.batch
    
class SalesTicket(models.Model):
    email = models.EmailField()
    telefone = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.email