from random import *
import random

'''Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears).'''

class Game(object):
    def __init__(self,lake_ecosystem_number):
        self._lake_ecosystem_number=lake_ecosystem_number
        self._bear_numbers=random.randint(0,6)
        self._fish_numbers=self._lake_ecosystem_number-self._bear_numbers
        self._lake=list(range(self._lake_ecosystem_number))

    def create_lake(self):
        z=0
        #populate the ecosystem with bears
        for i in range(len(self._lake)):
            if self._lake[i]!= 'B':
                 self._lake[random.randint(0, self._lake_ecosystem_number) - 1]= 'B'
        #populate the ecosystem with none elements
        print(self._bear_numbers)
        while z<self._lake_ecosystem_number-self._bear_numbers:
            if self._bear_numbers>0:
                self._lake[random.randint(0, self._lake_ecosystem_number - self._bear_numbers)]=None
                z+=1
            else:
                self._lake[random.randint(0, self._lake_ecosystem_number - self._bear_numbers-1)]=None
                z+=1
        #populate the ecosystem with fish
        for i in range(len(self._lake)):
            if self._lake[i]!= 'B' and self._lake[i]!=None:
                self._lake[i]= 'F'
        print(self._lake)

    def move_animal(self,animal_name):
        '''Function created in order to move a animal
        if a bear it's moved on a fish position the bear will replace
        the fish on it's position,if a bear/fish will move on a same animal position
        it will replace the first none element in the list'''
        n=random.randint(0,self._lake_ecosystem_number-1)
        if self._lake[n]!=animal_name:
            if self._lake[n]=='F':
                self._lake[n]='B'
            elif self._lake[n]==None:
                self._lake[n]=animal_name
            elif self._lake[n]==animal_name:
                for i in range(len(self._lake)):
                    if self._lake[i]==None:
                        self._lake[i]==animal_name
                        break


        print(self._lake)





for i in range(10):
    object1=Game(10)
    object1.create_lake()
    object1.move_animal('B')
