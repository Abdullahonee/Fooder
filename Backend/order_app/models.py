from django.db import models
from item_app.models import ItemList
from user_app.models import User
from user_app.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderlist')
    item = models.ForeignKey(ItemList, on_delete=models.CASCADE, related_name='orderlist')
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    is_confirmed = models.BooleanField(default=True)
    extra = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS = ['quantity', 'total_price']
    
    def __str__(self):
        return str(self.id) + " | " + self.user.username
    