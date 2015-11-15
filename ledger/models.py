from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


# Create your models here.
class Expense(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    @models.permalink
    def get_absolute_url(self):
        return ('expense_detail')

    @models.permalink
    def get_delete_url(self, **kwargs):
        return ('expense_delete')
