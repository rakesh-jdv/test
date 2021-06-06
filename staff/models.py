from django.db import models

class staff(models.Model):
    staff_code = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name


