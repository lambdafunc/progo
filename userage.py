#!/usr/bin/env python2.7
from datetime import datetime

now = datetime.now()
yr = now.year

def namenage():
    name = str(raw_input("Enter name:"))
    age = int(raw_input("Greetings, {} and How about your age:".format(name)))
    year = yr + (100 - int(age))
    print("In year {}, you will be 100 yr old".format(int(year)))

namenage()
