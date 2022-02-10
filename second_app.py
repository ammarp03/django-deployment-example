# from doctest import FAIL_FAST
# import email
import os
# from posixpath import split
# from unicodedata import name

# from matplotlib.style import use

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

import django
django.setup()

#fake POP  script

import random 

from  base.models import AccessRecord,Webpage,Topic2,User2

from faker import Faker

fakegen = Faker()

# topics = ['Search', 'Social', 'Marketplace', 'News', 'Games'] 

# def add_topic():
#     t = Topic2.objects.get_or_create(name = random.choice(topics))[0]
#     t.save()
#     return t


def populate(N=5):
    for entry in range(N):

        #get topic for entry

        # top = add_topic()

        #create fake data for that entry

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        #create a new webpage

        users = User2.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

        
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("Populating Complete!")

    
