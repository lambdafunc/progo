#!/usr/bin/env python
import random

health = 50
difficulty = 2
potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health
print health
