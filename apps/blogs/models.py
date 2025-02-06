from django.db import models

from utils.base_model import AbstractBaseModel
from utils.validators import check_fullname, clean_spaces


class Blog(AbstractBaseModel):
    """
      A model representing a blog post.

      Attributes:
          title (str): The title of the blog post.
          author (str): The name of the author, validated using `check_fullname`.
          category (str): The category to which the blog post belongs.
          description (str): A detailed description of the blog post (up to 5000 characters).

      Methods:
          clean(): Validates the `author` field using `check_fullname`.
          save(*args, **kwargs): Cleans spaces in `title`, `author`, and `category` before saving.
      """

    title = models.CharField(max_length=255)
    author = models.CharField(
        max_length=255,
        validators=[check_fullname]
    )
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)

    def clean(self):
        self.author = check_fullname(self.author)

    def __str__(self):
        return self.title
