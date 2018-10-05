# Django imports

from math import sin, cos, sqrt, atan2, radians

import os
from django.db import models
from django.db.models import F
from django.contrib.auth import get_user_model
import boto
from .models import Job

User = get_user_model()

boto_key = os.environ.get("BOTO_PUB_KEY")
boto_s_key = os.environ.get("BOTO_SECRET_KEY")

# conn = boto.connect_s3(boto_key, boto_s_key)
# bucket = conn.get_bucket('mobility-hack-new')
# k = Key(bucket)

def s3_delete(user_id, file_name):
    k.key = '/datasets/user_{0}/{1}'.format(user_id, file_name)
    k.delete()


def s3_upload(file, user_id, has_header, file_name):
    """Uploads a user's file to the user folder in S3"""

    k.key = '/datasets/user_{0}/{1}'.format(user_id, file_name)
    k.set_contents_from_filename(file_name)  # /from_file...





