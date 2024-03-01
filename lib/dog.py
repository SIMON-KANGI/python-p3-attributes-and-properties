#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed
        
    def get_name(self):
        print("getting name")
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print("Setting name")
            self._name=name
            print(name)
        else:
            print('Name must be string between 1 and 25 characters.')
        
    name=property(get_name,set_name)

    def get_breed(self):
        print("getting breed")
        return self.get_breed
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print("setting breed")
            self._breed=breed
            print(breed) 
        else:
                print("Breed must be in list of approved breeds." )
    
    breed=property(get_breed, set_breed)
fuda=Dog(name="Men", breed="Beagle")
fuda.name="Simon"
fuda.breed="Beagle"