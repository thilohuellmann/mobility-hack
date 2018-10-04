from django.db import models
from django.db.models import F
from django.contrib.auth import get_user_model

User = get_user_model()

GENDERS = (
        ('m', 'male'),
        ('f', 'female'),
        ('d', 'diverse'),
    )

RADII = (
    (1, '1km'),
    (2, '2km'),
    (5, '5km'),
    (10, '10km'),
)

class Supporter(models.Model):

    # id auto-increment is created automatically...
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDERS, max_length=255)
    birth_date = models.DateField()
    lat = models.FloatField()
    lng = models.FloatField()
    bio = models.CharField(max_length=1200)
    phone = models.CharField(max_length=20)
    radius = models.IntegerField(choices=RADII)

class Senior(models.Model):

    # id auto-increment is created automatically...
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=255)
    birth_date = models.DateField()
    lat = models.FloatField()
    lng = models.FloatField()
    bio = models.CharField(max_length=1200, null=True, blank=True)
    phone = models.CharField(max_length=20)

JOB_STATI = (
    ('draft', 'draft'),
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('done', 'done'),
    ('expired', 'expired'),
)

JOB_TYPES = (
    ('one_way', 'one_way'),
    ('round_trip', 'round_trip'),
)

# Arzt, Apotheke, Einkaufen, Kaffeekraenzchen, Bingo
# Apotheken Umschau -> Marketing

START_TIME_TYPES = (
    ('fixed', 'fixed'),
    ('flexible', 'flexible'),
)

TIME_SLOTS = (
    ('morning', 'morning'),
    ('noon', 'noon'),
    ('afternoon', 'afternoon'),
    ('evening', 'evening'),
)

class Job(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    senior_id = models.IntegerField()
    rated = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=JOB_STATI, default='draft')
    job_type = models.CharField(max_length=255, choices=JOB_TYPES)

    start_time_type = models.CharField(max_length=255, choices=START_TIME_TYPES, null=True)
    date = models.DateField(null=True) # datetime.date.today()
    time = models.TimeField(null=True) # datetime.time
    time_slot = models.CharField(max_length=255, choices=TIME_SLOTS, null=True)
    supporter_id = models.IntegerField(null=True)

class Rating(models.Model):
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField()

APPLICATION_STATI = (
    ('applied', 'applied'),
    ('confirmed', 'confirmed'),
    ('rejected', 'rejected'),
)

class Application(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_id = models.IntegerField()
    supporter_id = models.IntegerField()
    senior_id = models.IntegerField()
    application_status = models.CharField(max_length=255, choices=APPLICATION_STATI, default='applied')
