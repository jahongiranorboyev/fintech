from django.db import models

from utils.base_model import AbstractBaseModel
from utils.validators import check_fullname


class Mentor(AbstractBaseModel):
    full_name = models.CharField(
        max_length=255,
        validators=[check_fullname]
    )
    specialty = models.CharField(max_length=50)
    image = models.ImageField(upload_to='mentors/%Y/%m/%d')


    def __str__(self):
        return self.full_name
