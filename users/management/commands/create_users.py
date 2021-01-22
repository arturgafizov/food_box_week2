from django.core.exceptions import ValidationError
import requests
from django.core.management.base import BaseCommand


from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        link_user = requests.get(
            'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'
        )
        users = link_user.json()
        print(users)

        for user in users:
            recipient = User.objects.filter(id=user['id']).first()
            try:
                d = {}
                d['username'] = user['email'].split('@')[0]
                d['last_name'] = user['info']['surname']
                d['first_name'] = user['info']['name']
                d['middle_name'] = user['info']['patronymic']
                d['email'] = user['email']
                d['address'] = user['city_kladr']
                d['phone_number'] = user['city_kladr']

                new_user = User.objects.update_or_create(defaults=d, id=user['id'])
                self.stdout.write("User successfully created_or_update")
            except ValidationError:
                print("Validation Error")
