from django.db import models

# Create your models here.

class productMainModel(models.Model):
    Title=models.TextField(max_length=100)
    Description=models.TextField(max_length=400)
    Price=models.IntegerField()
    image=models.ImageField(upload_to='images')


    def __str__(self):
        return self.Title


class productColourModel(models.Model):
    Product= models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Colour =models.CharField(max_length=20)

    def __str__(self):
        return self.Colour

class productImageModel(models.Model):
    Product= models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.image