from django.db import models
from django.utils import timezone

# Create your models here.
class JewelVariety(models.Model):
    JEWEL_TYPE_CHOICE = [
        ('ER', 'EARINGS'),
        ('NL', 'NECKLACE'),
        ('RG', 'RINGS'),
        ('NS', 'NOSEPINS'),
        ('TP', 'TOPS'),
    ]
    
    name = models.CharField(max_length = 100 )
    image = models.ImageField(upload_to = 'firsts/' )
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length = 2, choices = JEWEL_TYPE_CHOICE)
    description = models.TextField(default = '')
    
    
    def __str__(self):
        return self.name
