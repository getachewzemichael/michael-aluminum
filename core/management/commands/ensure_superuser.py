import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update the Django superuser from environment variables."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get(
            "DJANGO_SUPERUSER_EMAIL", "michaeltadessemiki@gmail.com"
        )
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")
        reset_password = os.environ.get(
            "DJANGO_SUPERUSER_RESET_PASSWORD", "false"
        ).lower() in ("1", "true", "yes")
        explicit_password = "DJANGO_SUPERUSER_PASSWORD" in os.environ

        User = get_user_model()
        user = User.objects.filter(username=username).first()

        if user is None:
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created."))
            return

        updated = False
        if user.email != email:
            user.email = email
            updated = True

        if reset_password or explicit_password:
            user.set_password(password)
            updated = True

        if updated:
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f"Superuser '{username}' updated.")
            )
        else:
            self.stdout.write(f"Superuser '{username}' already exists.")
