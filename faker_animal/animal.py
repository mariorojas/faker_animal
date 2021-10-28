from random import choice

from faker.providers import BaseProvider

from .constants import animal_list


class AnimalProvider(BaseProvider):
    """
    A provider for animal-related names.

    >>> from faker import Faker
    >>> from faker_animal import AnimalProvider
    >>> fake = Faker()
    >>> fake.add_provider(AnimalProvider)
    >>> fake.animal()
    """

    def animal(self) -> str:
        return choice(animal_list)
