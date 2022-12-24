from user_app.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from item_app.models import ItemList


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewlist')
    item = models.ForeignKey(
        ItemList, on_delete=models.CASCADE, related_name="reviewlist")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=500, null=True)
    user_reply = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    REQUIRED_fIELDS = ['rating',]

    def __str__(self):
        return str(self.rating) + " | " + self.ItemList.title
