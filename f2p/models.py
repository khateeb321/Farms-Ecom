from django.db import models

# Create your models here.
class City(models.Model):
    label=models.CharField(max_length=250)

    def __str__(self):
        return  self.label


class Area(models.Model):
    label=models.CharField(max_length=250)
    city_label=models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return self.label+"\t"+self.city_label.label

class Veges(models.Model):
    label=models.CharField(max_length=250)
    price=models.IntegerField()
    img=models.CharField(max_length=250)
    def __str__(self):
        return  str(self.price)+"\t"+self.label

class Fruits(models.Model):
    label=models.CharField(max_length=250)
    price=models.IntegerField()
    img=models.CharField(max_length=250)
    def __str__(self):
        return  self.label
class farmDesciption(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=500)
    age=models.CharField(max_length=25)
    contcNum=models.IntegerField()
    land_owner=models.IntegerField()
    area=models.CharField(max_length=250)
    img=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class fruitFarm(models.Model):
    fruit=models.ForeignKey(Fruits,on_delete=models.CASCADE)
    farm=models.ForeignKey(farmDesciption,on_delete=models.CASCADE)
    def __str__(self):
        return self.farm.name+self.farm.description+str(self.farm.age)+str(self.farm.contcNum)+self.farm.area+self.farm.img

class vegeFarm(models.Model):
    vege=models.ForeignKey(Veges,on_delete=models.CASCADE)
    farm=models.ForeignKey(farmDesciption,on_delete=models.CASCADE)

    def __str__(self):
        return self.farm.name+"\t"+self.farm.description+"\t"+str(self.farm.age)+"\t"+str(self.farm.contcNum)+"\t"+self.farm.area+"\t"+self.farm.img

class nutrientsVeges(models.Model):
    vege=models.ForeignKey(Veges,on_delete=models.CASCADE)
    carbohydrates=models.FloatField()
    proteins=models.FloatField()
    energy=models.FloatField()
    fats = models.FloatField()
    sugar = models.FloatField()
    potassium = models.FloatField()
    iron = models.FloatField()
    calcium = models.FloatField()
    def __str__(self):
        return self.vege.label

class registeredUser(models.Model):
    userName=models.CharField(max_length=400)
    area=models.ForeignKey(Area,on_delete=models.CASCADE)
    address=models.CharField(max_length=400)
    contactNum=models.CharField(max_length=400)
    email=models.CharField(max_length=250)
    def __str__(self):
        return self.userName+"\t"+self.area.label+"\t"

class orderDetails(models.Model):
    user = models.ForeignKey(registeredUser, on_delete=models.CASCADE)
    orderID = models.IntegerField()
    status = models.CharField(max_length=10)
    cost = models.FloatField()
    odate = models.DateField()
    def __str__(self):
        return self.user.userName+"\t"+self.status+"\t"+str(self.cost)

class fruitOrder(models.Model):
    orderID=models.ForeignKey(orderDetails,on_delete=models.CASCADE)
    fruit=models.ForeignKey(Fruits,on_delete=models.CASCADE)
    def __str__(self):
        return self.fruit.label+"\t"+str(self.orderID.orderID)

class vegeOrder(models.Model):
    orderID=models.ForeignKey(orderDetails,on_delete=models.CASCADE)
    vege=models.ForeignKey(Veges,on_delete=models.CASCADE)
class nutrientsFruits(models.Model):
    fruit=models.ForeignKey(Fruits,on_delete=models.CASCADE)
    carbohydrates=models.FloatField()
    proteins=models.FloatField()
    energy=models.FloatField()
    fats = models.FloatField()
    sugar = models.FloatField()
    potassium = models.FloatField()
    iron = models.FloatField()
    calcium = models.FloatField()
    def __str__(self):
        return self.fruit.label