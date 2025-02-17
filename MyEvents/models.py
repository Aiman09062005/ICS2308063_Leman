from django.db import models

# Create your models here.

class Events(models.Model):
    eventid = models.CharField(max_length=7, primary_key=True)
    eventname = models.TextField()
    eventdate = models.DateField()
    venue = models.TextField()
    maxattendees = models.CharField(max_length=4)
    eventstatus = models.CharField(max_length=20, default='Scheduled')

class Participants(models.Model):
    participantid = models.CharField(max_length=4, primary_key=True)
    participantname = models.CharField(max_length=20)
    participantphone = models.CharField(max_length=10)
    participantemail = models.EmailField(default='default@example.com')

class Registrations(models.Model):
    eventid = models.ForeignKey(Events, on_delete=models.CASCADE)
    participantid = models.ForeignKey(Participants, on_delete=models.CASCADE)
    registrationdate = models.DateField()
    ticketnumber = models.CharField(max_length=10)
    amountpaid = models.IntegerField()