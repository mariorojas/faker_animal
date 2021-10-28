import pytest
from faker import Faker

from faker_animal import AnimalProvider
from faker_animal.constants import animal_list


@pytest.fixture
def fake():
    fake = Faker()
    fake.add_provider(AnimalProvider)
    return fake


def test_animal_list():
    assert len(animal_list) > 1


def test_animal_name_length(fake):
    for _ in range(0, len(animal_list)):
        name = fake.animal()
        assert len(name) > 1, f'Animal name {name} is too short'


def test_animal_name_capitalized(fake):
    for _ in range(0, len(animal_list)):
        name = fake.animal()
        capitalized = name.capitalize()
        assert capitalized == name, f'Animal name {name} is not capitalized'
