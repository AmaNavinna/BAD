from django.db import models

# Create your models here.

class NowShowingMovie(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="pics", default="default.png")
    date = models.DateField()
    duration = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    cast = models.TextField(max_length=100)
    trailer = models.CharField(max_length=100)
    up = models.BooleanField(default=False)
    id = models.BigAutoField(primary_key=True)

# Define a model for upcoming movies
class UpcomingMovie(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="pics", default="default.png")
    date = models.DateField()
    duration = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    cast = models.TextField(max_length=100)
    trailer = models.CharField(max_length=100)
    release_date = models.DateField()
    id = models.BigAutoField(primary_key=True)

class Reg(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    age = models.IntegerField()
    seats = models.IntegerField()
    id = models.BigAutoField(primary_key=True)

# Define a model for user contacts
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.name

# Define a model for transactionsx
class Transaction(models.Model):
    date = models.DateField()
    movie = models.ForeignKey(NowShowingMovie, on_delete=models.CASCADE)
    show_time = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    seat_number = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)
    card_holder_name = models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return f"{self.user_name} - {self.movie.name} - {self.date}"



