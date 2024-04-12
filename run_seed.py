import django
django.setup()

from about.seed import *
from skills.seed import *
from portfolio.seed import *
from services.seed import *
from testimonials.seed import *
from contact.seed import *

if __name__== '__main__':
    run()
    # run2()
    # run3()
    # run4()
    # run5()
    # run6()
