from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя пользователя", null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name="Номер телефона", unique=True)

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.phone

    def __unicode__(self):
        return self.name


class Store(models.Model):
    store_name = models.CharField(max_length=200, verbose_name="Название Торговой точки ")
    employee = models.ForeignKey(Employee, models.CASCADE, related_name='staff')

    class Meta:
        verbose_name = "Торговая точка"
        verbose_name_plural = "Торговые точки"

    def __str__(self):
        return self.store_name

    def __unicode__(self):
        return self.store_name


class StoreVisitLog(models.Model):
    store = models.ForeignKey(Store, models.CASCADE, related_name='shop')
    visited_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

    def __str__(self):
        return f'{self.visited_at}'

