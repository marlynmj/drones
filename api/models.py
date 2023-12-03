from django.db import models
from django.db.models import Max
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
MODELO = (
        ("li", "light"),
        ("me", "medium"),
        ("cr", "cruiser"),
        ("he", "heavy"),
)

WEIGHT_LIMIT = [MinValueValidator(0), MaxValueValidator(500)]
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

STATUS = (
        ("id", "IDLE"),
        ("log", "LOADING"),
        ("lod", "LOADED"),
        ("deg", "DELIVERING"),
        ("ded", "DELIVERED"),
        ("ret", "RETURN"),
)

alphanumeric = RegexValidator(r'^[0-9a-zA-Z_-]*$', 'Only alphanumeric characters, underscore and middlescore are allowed.')

alphanumericCode = RegexValidator(r'^[0-9A-Z_]*$', 'Only alphanumeric characters and underscore are allowed.')

class Dron(models.Model):
    serialNumber = models.CharField(max_length=150)
    model = models.CharField(choices=MODELO, default=0, max_length=2)
    weightLimit = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=WEIGHT_LIMIT)
    batteryCapacity = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)
    status = models.CharField(choices=STATUS, default=0, max_length=3)
    
    def __unicode__(self):
        return self.serialNumber

class Drug(models.Model):
    name = models.CharField(validators=[alphanumeric], max_length=250)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    code = models.CharField(validators=[alphanumericCode], max_length=250)
    image = models.ImageField(upload_to='imagenes', null=True, blank=True)
#     dron = models.ManyToManyField(Dron, null = True, blank = True)
    dron = models.ForeignKey(Dron, on_delete=models.CASCADE, null = True, blank = True)
    
    def __unicode__(self):
        return self.name
    
class Historial(models.Model):
    dron = models.ForeignKey(Dron, on_delete=models.CASCADE, null = True, blank = True)
    batteryLevel = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)
    dayTime = models.DateTimeField()
    
    def __unicode__(self):
        return self.dron__serialNumber