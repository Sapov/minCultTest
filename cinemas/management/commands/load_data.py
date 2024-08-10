from cinemas.management.commands.validators import parse_data
from django.core.management.base import BaseCommand
from cinemas.models import CinemaGeneral


def str_cleaning(st: str) -> str:
    return st.replace('<p>', '').replace('</p>', '').replace('<br />', '')


class Command(BaseCommand):

    def handle(self, *args, **options):
        for data in parse_data().data:
            print(data.data.general.id)
            if data.data.general.contacts and data.data.general.contacts.phones:
                print(data.data.general.contacts.website)
                print(data.data.general.contacts.email)
                print(data.data.general.contacts.phones[0].value)
                CinemaGeneral.objects.get_or_create(
                    id_service=data.data.general.id,
                    name=data.data.general.name,
                    description=str_cleaning(data.data.general.description),
                    street=data.data.general.address.street,
                    comment=data.data.general.address.comment,
                    full_address=data.data.general.address.fullAddress,
                    category=data.data.general.category.name,
                    category_sysName=data.data.general.category.sysName,
                    website=data.data.general.contacts.website,
                    email=data.data.general.contacts.email,
                    phones=data.data.general.contacts.phones[0].value)
