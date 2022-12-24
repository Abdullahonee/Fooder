from django.db import models
from user_app.models import User
from location.models import Locations


# def validate_decimals(value):
#     try:
#         return round(float(value), 2)
#     except:
#         raise ValidationError(
#             ('%(value)s is not an integer or a float  number'),
#             params={'value': value},
#         )


class ItemList(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    total_available = models.IntegerField()
    # image = models.ImageField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='itemlist', null=False)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='location', null=False)
    order_count = models.IntegerField(default=0)
    total_sold = models.IntegerField(default=0)
    Description = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    # avg_rating = models.FloatField(default=0, validators=[validate_decimals])
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_fIELDS = ['title', 'total_available', 'price', 'location',]

    # def save(self, *args, **kwargs):
    #     self.avg_rating = round(self.avg_rating, 2)
    #     super(ItemList, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
