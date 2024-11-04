from django.db import models
from django.contrib.auth.models import User


# class Tour(models.Model):
#     title = models.CharField(max_length=255)  # Ensure this field exists
#     duration = models.IntegerField()  # Ensure this field exists
#     created_at = models.DateTimeField(auto_now_add=True)  # Ensure this field exists
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     image = models.ImageField(upload_to='tours/images')

#     def __str__(self):
#         return self.title

class Tour(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='tours/images')
    
    # New fields for storing the tour's location
    latitude = models.FloatField(null=True, blank=True)  # Allowing null values initially
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    tour = models.ForeignKey(Tour, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.text}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.tour.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='path/to/default/image.jpg')
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Add this field
    address = models.TextField(blank=True, null=True)  # Add this field

    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

