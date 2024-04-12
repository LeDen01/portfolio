from contact.models import *
from django_seed import Seed

def run6():
    seeder = Seed.seeder()
    
    contact = {
        'location' : 'New York, USA',
        'email' : 'email@example.com',
        'phone' : '+1 5589 55488 55'
    }

    seeder.add_entity(Contact, 1, contact)
    
    seeder.execute()