import json
from typing import Optional

from pydantic import BaseModel, EmailStr


class Phones(BaseModel):
    value: Optional[str] = None
    comment: Optional[str] = None


class Gallery(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None


class Contacts(BaseModel):
    website: Optional[str] = None
    email: Optional[str] = None
    phones: Optional[list[Phones]] = None


class Category(BaseModel):
    name: str
    sysName: str


class MapPosition(BaseModel):
    type: str
    coordinates: list


class Address(BaseModel):
    street: str
    comment: str | None
    fullAddress: str
    mapPosition: MapPosition


class General(BaseModel):
    id: int
    name: str
    description: str
    address: Address
    category: Category
    contacts: Optional[Contacts] = None
    gallery: Optional[list[Gallery]] = None


class Data1(BaseModel):
    info: dict
    general: General


class Data(BaseModel):
    hash: str
    data: Data1


class Cinema(BaseModel):
    status: int
    total: int
    data: list[Data]


def parse_data():
    with open('/home/sasha/PycharmProjects/test_mincult/cinemas/management/commands/cinema.json', 'r',
              encoding='utf-8') as file:
        data = json.load(file)

    cinema = Cinema(**data)
    for i, data in enumerate(cinema.data):
        if data.data.general.contacts:
            print(f'# {i} val {data.data.general.contacts}'
                  f'id_service = {data.data.general.id}',
                  f'name = {data.data.general.name}',
                  f'description = {data.data.general.description}',
                  f'street = {data.data.general.address.street}',
                  f'comment={data.data.general.address.comment}',
                  f'full_address={data.data.general.address.fullAddress}',
                  f'category={data.data.general.category.name}',
                  f'category_sysName={data.data.general.category.sysName}',
                  f'website={data.data.general.contacts.website}',
                  f'email={data.data.general.contacts.email}',
                  f'phones={data.data.general.contacts.phones}',
                  f'type={data.data.general.address.mapPosition.type}'
                  )

    return cinema


if __name__ == '__main__':
    parse_data()

# try:
#     cinema = Cinema(**data)
#     print(cinema.data[0].data.general.contacts)
#
# except ValidationError as exc:
#     print(exc.json())
# print(repr(exc.errors()[0]['type']))
# > 'missing'
