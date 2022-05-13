from django.db import models

# Create your models here.

class Order(models.Model):
    order_at = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200,verbose_name='Phone')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name ='Order'
        verbose_name_plural = 'Orders'
        
class TelebotSettings(models.Model):
    token = models.CharField(max_length=200, verbose_name='TOKEN')
    chat_id = models.CharField(max_length=200, verbose_name= 'Chat ID')
    text = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.chat_id

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'