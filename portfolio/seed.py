from portfolio.models import *
from django_seed import Seed

def run3():
    seeder = Seed.seeder()

    portfolio = [
        {
            'image' : 'images/portfolio-1.jpg',
            'filter' : 'app'
        },
        {
            'image' : 'images/portfolio-2.jpg',
            'filter' : 'web'
        },
        {
            'image' : 'images/portfolio-3.jpg',
            'filter' : 'app'
        },
        {
            'image' : 'images/portfolio-4.jpg',
            'filter' : 'card'
        },
        {
            'image' : 'images/portfolio-5.jpg',
            'filter' : 'web'
        },
        {
            'image' : 'images/portfolio-6.jpg',
            'filter' : 'app'
        },
        {
            'image' : 'images/portfolio-7.jpg',
            'filter' : 'card'
        },
        {
            'image' : 'images/portfolio-8.jpg',
            'filter' : 'card'
        },
        {
            'image' : 'images/portfolio-9.jpg',
            'filter' : 'web'
        }
    ]
    
    for item in portfolio:
        seeder.add_entity(Portfolio, 1, item)

    seeder.execute()
