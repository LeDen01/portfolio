from about.models import *
from django_seed import Seed

def run():
    seeder = Seed.seeder()
    
    pnj = {
        'description' : 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'title' : 'UI/UX Designer & Web Developer.',
        'about' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'more' : 'Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.',
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
    seeder.execute()