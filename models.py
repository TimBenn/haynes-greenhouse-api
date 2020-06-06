from mongoengine import ListField, StringField, BooleanField, EmailField, IntField, Document, ReferenceField
import datetime

class Device(Document):
  name = StringField(required=True, max_length=50)

class Greenhouse(Document):
  devices = ListField(ReferenceField(Device))
  routines = ListField(required=False)
  name = StringField(required=True, max_length=50)

class Account(Document):
  greenhouses = ListField(ReferenceField(Greenhouse))
  first_name = StringField(required=False)
  last_name = StringField(required=False)
  email = EmailField(required=True, unique=True)
  address_line_1 = StringField(required=False)
  address_line_2 = StringField(required=False)
  city = StringField(required=False)
  state = IntField(required=False)
  zipcode = StringField(required=False)
  active = BooleanField(required=False, default=False)