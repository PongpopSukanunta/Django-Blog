from django.apps import AppConfig
from PIL import Image


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img.thumbnail(output_size)
            img.save(self.image.path)
