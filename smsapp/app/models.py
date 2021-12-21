import os
from django.db import models
from twilio.rest import Client

# Create your models here.

class UserText(models.Model):
    number_to = models.CharField(max_length=11)
    # text_message = models.CharField(max_length=160)
    

    def send_text(self, *args, **kwargs):

        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        number_from = os.environ['TWILIO_NUMBER']
        messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID']

       
        client = Client(account_sid, auth_token)

        message = client.messages.create(  
                              messaging_service_sid,
                              body='test',      
                              to='+17173412994' 
                          ) 

        print(message.sid)
        return super().save(*args, **kwargs)



    def __str__(self):
        return '{}'.format( self.number_to) 



