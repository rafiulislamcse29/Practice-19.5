from django.db import models

# Create your models here.
class Musician(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  email=models.EmailField()
  phone_no=models.CharField(max_length=12)
  instrument_choice = [
    ('percussion', 'Percussion'),
    ('woodwind', 'Woodwind'),
    ('string', 'String'),
    ('brass', 'Brass'),
    ('keyboard', 'Keyboard'),
    ]
  instrument_type = models.CharField(max_length=50, 
 choices=instrument_choice, default='-------')

  def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"
