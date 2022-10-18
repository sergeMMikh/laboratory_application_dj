from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    telephone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.surname}"


class Furnace(models.Model):
    # furnace name in laboratory specifications
    furnace_name = models.CharField(max_length=50)

    # location in laboratory
    location = models.CharField(max_length=50,
                                verbose_name='location')

    # technical furnace conditions: is it working (Tru) or broken (False)
    serviceable = models.BooleanField(verbose_name='available to use')

    # the maximum operating temperature
    max_temperature = models.PositiveIntegerField(verbose_name='max. temperature')

    # the minimum operating temperature
    min_temperature = models.PositiveIntegerField(verbose_name='min. temperature')

    # is furnace using for clean materials: free from acids, alkaline, transition or volatilizing elements
    is_clean = models.BooleanField(verbose_name='for clean materials')

    # the current furnace user
    user = models.ManyToManyField(Person,
                                  related_name='furnaces',
                                  through='BookingOfFurnace')

    def __str__(self):
        return self.furnace_name


class BookingOfFurnace(models.Model):
    date = models.DateField()
    furnace = models.ForeignKey(
        Furnace,
        on_delete=models.CASCADE,
        related_name='furnace',
    )

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='user',
    )

    class Meta:
        constraints = [models.UniqueConstraint(name='unique_booking',
                                               fields=['date',
                                                       'person',
                                                       'furnace'])]
