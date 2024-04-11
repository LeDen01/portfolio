from services.models import *
from django_seed import Seed


def run4():
    seeder = Seed.seeder()
    
    services = [
        {
            'icone' : 'bi bi-briefcase',
            'title' : 'Lorem Ipsum',
            'description' : 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident'
        },
        {
            'icone' : 'bi bi-card-checklist',
            'title' : 'Dolor Sitema',
            'description' : 'Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata'
        },
        {
            'icone' : 'bi bi-bar-chart',
            'title' : 'Sed ut perspiciatis',
            'description' : 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur'
        },
        {
            'icone' : 'bi bi-binoculars',
            'title' : 'Magni Dolores',
            'description' : 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
        },
        {
            'icone' : 'bi bi-brightness-high',
            'title' : 'Nemo Enim',
            'description' : 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque'
        },
        {
            'icone' : 'bi bi-calendar4-week',
            'title' : 'Eiusmod Tempor',
            'description' : 'Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi'
        }
    ]

    for item in services:
        seeder.add_entity(Service, 1, item)

    seeder.execute()
