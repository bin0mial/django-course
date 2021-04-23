from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from books.models import Book, ISBN


@receiver(post_save, sender=Book)
def create_default_profile(sender, instance: Book, created, **kwargs):
    if created:
        instance.ISBN = ISBN.objects.create(book_title=instance.title, author_title=instance.owner.username)
        instance.save()


@receiver(post_save, sender=User)
def give_permission_read_to_new_user(sender, instance: User, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Book)
        permissions = Permission.objects.filter(content_type=content_type)
        permission = permissions.filter(name__icontains="Can view book").get()
        print(permission)
        instance.user_permissions.add(permission)
