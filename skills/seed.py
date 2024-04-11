from skills.models import *
from django_seed import Seed

def run2():
    seeder = Seed.seeder()
    
    skills = [
        {
            "langage" : "HTML",
            "level" : 100
        },
        {
            "langage" : "CSS",
            "level" : 100
        },
        {
            "langage" : "JAVASCRIPT",
            "level" : 80
        },
        {
            "langage" : "PHP",
            "level" : 60
        },
        {
            "langage" : "WORDPRESS",
            "level" : 70
        },
        {
            "langage" : "PHOTOSHOP",
            "level" : 55
        }
    ]
    
    for item in skills:
        seeder.add_entity(Skills, 1, item)

    seeder.execute()
