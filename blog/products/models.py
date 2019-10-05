from django.db import models
class Product(models.Model):
	title =models.CharField(max_length=222)
	description =models.TextField()
	price =models.DecimalField(decimal_places=2,max_digits=225)
	summary =models.TextField(blank=False)