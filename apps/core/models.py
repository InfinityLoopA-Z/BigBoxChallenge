# Create your models here.
from django.db import models


class Common(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    slug = models.SlugField()

    class Meta:
        abstract = True


class CommonInfo(Common):

    class Meta:
        abstract = True


class Reason(CommonInfo):
    order = models.IntegerField(default=0, verbose_name='orden')


class Category(CommonInfo):
    order = models.IntegerField(default=0, verbose_name='orden')
    description = models.TextField(verbose_name=u'descripción')
    color = models.CharField(max_length=200, default='FFFFFF')


class Image(models.Model):
    order = models.IntegerField(default=0, verbose_name='orden')
    upload = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name='imagen')

    class Meta:
        abstract = True


class Product(Common):
    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    description = models.TextField(verbose_name=u'descripción')
    category = models.ForeignKey(Category, verbose_name='categoría', on_delete=models.CASCADE, null=True, blank=True)
    purchase_available = models.BooleanField(verbose_name='disponible venta individual', default=True)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True


class Activity(Product):
    reasons = models.ManyToManyField(Reason, verbose_name='tags', blank=True)


class Box(Product):
    activities = models.ManyToManyField(Activity)
    participant_number = models.IntegerField(default=1, verbose_name='numero de participantes')
    price = models.DecimalField(verbose_name='precio de venta', decimal_places=2, max_digits=6)


class ActivityImage(Image):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)


class BoxImage(Image):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
