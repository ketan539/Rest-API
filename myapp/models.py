from django.db import models

class user(models.Model):
    client_name=models.CharField(max_length=100)
    id=models.IntegerField
    create_date=models.DateTimeField
    user_name=models.CharField(max_length=100)
    # mobile_no=models.CharField(max_length=100)



