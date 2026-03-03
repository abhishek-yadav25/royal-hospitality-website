from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    event_date = models.DateField()
    guests = models.IntegerField()
    event_type = models.CharField(max_length=50)
    requirements = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name