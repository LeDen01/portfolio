from testimonials.models import *
from django_seed import Seed

def run5():
    seeder = Seed.seeder()
    
    temoignages = [
        {
            'auteur' : 'Saul Goodman',
            'poste' : 'Ceo &amp; Founder',
            'description' : 'Proin iaculis purus consequat sem cure digni ssim donec porttitor entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.',
            'image' : 'images/testimonials-1.jpg'
        },
        {
            'auteur' : 'Sara Wilsson',
            'poste' : 'Designer',
            'description' : 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.',
            'image' : 'images/testimonials-2.jpg'
        },
        {
            'auteur' : 'Jena Karlis',
            'poste' : 'Store Owner',
            'description' : 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.',
            'image' : 'images/testimonials-3.jpg'
        },
        {
            'auteur' : 'Matt Brandon',
            'poste' : 'Freelancer',
            'description' : 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.',
            'image' : 'images/testimonials-4.jpg'
        },
        {
            'auteur' : 'John Larson',
            'poste' : 'Entrepreneur',
            'description' : 'Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.',
            'image' : 'images/testimonials-5.jpg'
        }
    ]

    for item in temoignages:
        seeder.add_entity(Temoignage, 1, item)

    seeder.execute()