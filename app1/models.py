from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.category_name}"

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    film_name = models.CharField(max_length=50)
    rating = models.IntegerField()
    date = models.DateField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.film_id} {self.film_name}"