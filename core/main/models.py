from django.db import models

# Create your models here.


class MeetingInfo(models.Model):

    talked_time = models.PositiveIntegerField('MeetInfo talking time')
    microphone_used = models.PositiveIntegerField('MeetInfo microfone used')
    speaker_used = models.PositiveIntegerField('MeetInfo speaker used')
    voice_sentiment = models.PositiveIntegerField('MeetInfo voice_sentiment')

    