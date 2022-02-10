# from doctest import FAIL_FAST
import os
from unicodedata import name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

import django
django.setup()

#fake POP  script

import random 

from  base.models import AccessRecord,Webpage,Topic2

from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games'] 

def add_topic():
    t = Topic2.objects.get_or_create(name = random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        #get topic for entry

        top = add_topic()

        #create fake data for that entry

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create a new webpage

        webpg = Webpage.objects.get_or_create(topic = top, url= fake_url, name= fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name= webpg, date= fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(N=20)
    print("Populating Complete!")

    
