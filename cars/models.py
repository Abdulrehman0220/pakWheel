from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

from django.db import models
# Create your models here.
class Car(models.Model):
    state_choice = (
        ('PU', 'Punjab'),
        ('KPK', 'Khaiybar Pakhthonkhan '),
        ('SI', 'Sindh'),
        ('Bl', 'Baluchistan'),
        ('FD', 'Federal'),
    )
    year_choice = []
    for r in range(200, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choice = (
        ('Cruise control', 'Cruisecontrol'),
        ('Audio Interface', 'Audio Interface'),
        ('AirBags', 'AirBags'),
        ('Seat Heating ', 'Seat Heating '),
        ('Alarm System', 'Alarm System'),
        ('PakAssist', 'PakAssist'),
        ('Power staring', 'Power staring'),
        ('Revers Camera', 'Revers Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto start/stop', 'Auto start/stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('BluetoothHandset ', 'BluetoothHandset'),
    )
    door_choices = (
        ('2', '2'),
        ('4', '4'),
        ('5', '5'),
    )
    car_title = models.CharField(max_length=250)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=250)
    colour = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.IntegerField('year', choices=year_choice)
    condition = models.CharField(max_length=250)
    description = RichTextField()
    price = models.IntegerField
    car_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    feautures = MultiSelectField(choices=features_choice)
    body_style = models.CharField(max_length=250)
    engine = models.CharField(max_length=250)
    transmision = models.CharField(max_length=250)
    interior = models.CharField(max_length=250)
    miles = models.IntegerField
    doors = models.CharField(choices=door_choices, max_length=100)
    passanger = models.CharField(max_length=250)
    vin_no = models.CharField(max_length=250)
    milage = models.CharField(max_length=250)
    fuel_type = models.CharField(max_length=250)
    no_of_owners = models.CharField(max_length=250)
    is_featured = models.BooleanField(max_length=250)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

