from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'person'

    def __str__(self) -> str:
        return self.name
