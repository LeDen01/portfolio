from about.models import *
from django_seed import Seed

def run():
    seeder = Seed.seeder()
    
    pnj = {
        'image': 'images/profile-img.jpg',
        'birthday': '1995-05-01',
        'age': 30,
        'website': 'www.example.com',
        'degree': 'Master',
        'phone': '+123 456 7890',
        'email': 'email@example.com',
        'city': 'New York, USA',
        'freelance': True
    }

    seeder.add_entity(Person, 1, pnj)