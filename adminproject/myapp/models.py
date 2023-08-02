from django.db import models

# Create your models here.

class product_master(models.Model):
    product_id=models.AutoField(primary_key=True)
    Brand_name=models.CharField(max_length=20)

    def __str__(self):
        return self.Brand_name
        

   

class product_categary(models.Model):
    product=models.ForeignKey(product_master,on_delete=models.CASCADE)
    price=models.IntegerField()
    image=models.ImageField(upload_to='file')
    model=models.CharField(max_length=20)
    ram=models.CharField(max_length=30)
    

