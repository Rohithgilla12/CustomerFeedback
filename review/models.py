from django.db import models

# Create your models here.

RatingChoices= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ]

class Review(models.Model):
    name = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)
    emailID = models.EmailField(max_length = 254)    
    mobileNumber = models.CharField(max_length = 10)
    rating = models.CharField(max_length =1, choices =RatingChoices )
    review = models.CharField(max_length= 200)
    city = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.emailID)

    