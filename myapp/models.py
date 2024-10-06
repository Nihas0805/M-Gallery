from django.db import models 

class GenreChoices(models.TextChoices):
    MYSTERY = 'Mystery','Mystery'
    ACTION = 'Action','Action'
    SCI_FI = 'Sci fi','Sci fi'

class Movies(models.Model):

    title=models.CharField(max_length=200,null=False,blank=False)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)


# class FuelChoices(model.TextChoices):
#     PETROL='Petrol','Petrol'
#     DIESEL='Diesel','Diesel'
#     EV='EV','EV'
#     HYBRID='Hybrid','Hybrid'



# class Car(models.Model):

#     name=models.CharField(max_length=200,null=False,blank=False)

#     model=models.CharField(max_length=200)

#     fuel_type=models.CharField(max_length=200,choices=FuelChoices.choices)

#     date=models.DateTimeField()

#     no_of_seats=models.PositiveIntegerField()

#     stock=models.BooleanField()

# class Customer(models.Model):

#     first_name=mosela.CharField(max_length=200,null=False,blank=False)

#     last_name=models.CharField(max_length=200)

#     street_address=models.CharField(max_length=200)

#     street_address_line2=models.CharField(max_length=200)

#     city=models.CharField(max_length=200)

#     state=models.CharField(max_length=200)

#     pincode=models.PositiveIntegerField(max_length=200)

#     ph_no=models.CharField(max_length=200)

#     email=models.CharField(max_length=200)

#     heard=models.CharField(max_length=200,choices=FuelChoices.choices)

#     date=models.DateTimeField()

#     no_of_seats=models.PositiveIntegerField()

#     stock=models.BooleanField()


    


# class ClassesChoices(models.IntegerChoices):
#     class1 = 1, 1
#     class2 = 2, 2
#     class3 = 3, 3
#     class4 = 4, 4
#     class5 = 5, 5
#     class6 = 6, 6
#     class7 = 7, 7
#     class8 = 8, 8
#     class9 = 9, 9
#     class10 = 10, 10

# class DivisionChoices(models.TextChoices):
#     div1='A','A'
#     div2='B','B'
#     div3='C','C'
#     div4='D','D'
#     div5='E','E'
    

# class Student(models.Model):

#     name=models.CharField(max_length=200)

#     classes=models.CharField(max_length=200,choices=ClassesChoices.choices)

#     division=models.CharField(max_length=200,choices=DivisionChoices.choices)

#     roll_no=models.CharField(max_length=200)

#     about_me=models.TextField()

#     image=models.ImageField()

#     url=models.URLField()



    

  