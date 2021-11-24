from django.contrib import admin

from apps.core import models


@admin.register(models.BoxImage)
class BoxImageModel(admin.ModelAdmin):
    pass


@admin.register(models.Box)
class BoxModel(admin.ModelAdmin):
    pass


@admin.register(models.ActivityImage)
class ActivityImage(admin.ModelAdmin):
    pass


@admin.register(models.Activity)
class Activity(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    pass


@admin.register(models.Reason)
class Reason(admin.ModelAdmin):
    pass
