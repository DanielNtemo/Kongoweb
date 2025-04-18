from django.db.models import *


class Information(Model):
    name = CharField(max_length=100,null=False,blank=False)
    adress = CharField(max_length=100, null=False, blank=False)
    id_number = CharField(max_length=100, null=False, blank=False)
    imp_exp_number = CharField(max_length=100, null=False, blank=False)

