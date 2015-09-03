#!/usr/local/bin/python
#
# test.py

class cake(object):
    def __init__(self, type, flavor, color):
        self.type = type
        self.flavor = flavor
        self.color = color

    def description(self):
        print "I'm a %s, %s, %s cake!" %(self.color, self.type, self.flavor)

test = cake("sponge", "strawberry", "red")
test.description()
