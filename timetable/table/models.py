from django.db import models

# Create your models here.


class Day(models.Model):
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )
    day_name = models.CharField('Day of the week', max_length=64, choices=DAYS)
    start_time = models.TimeField('Start')
    end_time = models.TimeField('End')
    subject = models.CharField('Subject Name', max_length=64)

    def __str__(self):
        return f"{self.day_name} from {self.start_time} to {self.end_time} for {self.subject}"
