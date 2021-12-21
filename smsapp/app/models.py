import os
from django.db import models
from twilio.rest import Client

# Create your models here.

class UserText(models.Model):
    number_to = models.CharField(max_length=11)
    # text_message = models.CharField(max_length=160)
    

    def send_text(self, *args, **kwargs):

        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        # number_from = os.environ['TWILIO_NUMBER']
        # messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID']

        account_sid = 'ACa3eafe7ea1d7040d6b255744e791df60'
        auth_token = '12e9b3b3daa0501ed2f514bce2a81bd8'
        messaging_service_sid = 'MG06e87a7afc7e5eed04c7b2ef47160038'
      

        client = Client(account_sid, auth_token)

        message = client.messages.create(  
                              messaging_service_sid='MG06e87a7afc7e5eed04c7b2ef47160038', 
                              body='sdfsdf',      
                              to='+17173412994' 
                          ) 

        # message = client.messages.create(
        #                         messaging_service_sid = 'MG06e87a7afc7e5eed04c7b2ef47160038',
        #                         body='test',
        #                         from_='+12345952762',
        #                         to='+17173412994'
        #                     )

        print(message.sid)
        return super().save(*args, **kwargs)



    def __str__(self):
        return '{}'.format( self.number_to) 



