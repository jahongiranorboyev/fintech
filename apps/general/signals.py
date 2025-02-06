import os

from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from django.db.models import CharField, TextField, ImageField, FileField

from utils import clean_spaces


@receiver(pre_save)
def pre_save_handler_char_text_fields(sender, instance, **kwargs):
    model_fields = instance._meta.get_fields()
    for field in model_fields:
        if isinstance(field, (CharField, TextField)):
            cleaned_value = clean_spaces(getattr(instance, field.name))
            setattr(instance, field.name, cleaned_value)


@receiver((post_delete, pre_save))
def delete_related_files(instance, sender, **kwargs):
    """
    Deletes related files when an instance is deleted or updated.

    Args:
        instance (Model instance): The model instance being saved or deleted.
        sender (Model class): The model class that triggered the signal.
        kwargs (dict): Additional keyword arguments passed by the signal.
    """
    for field in sender._meta.get_fields():
        if isinstance(field, (ImageField, FileField)):
            file = getattr(instance, field.name)

            if kwargs['signal'] == post_delete:
                if file and os.path.exists(file.path):
                    os.remove(file.path)

            elif kwargs['signal'] == pre_save:
                if instance.pk:
                    old_instance = sender.objects.filter(pk=instance.pk).first()
                    if old_instance:
                        old_file = getattr(old_instance, field.name)
                        if old_file and old_file != file and os.path.exists(old_file.path):
                            os.remove(old_file.path)
