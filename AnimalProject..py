from pprint import pprint


class Animals(object):
    '''Animal class implemented in other what noise is making each animal'''
    def __init__(self,animalList,sounds):
        self.animalList=animalList
        self.sounds=sounds

    def noises(self):
        for i in range(len(self.animalList)):
                print("The {0} is making the noise {1} \n".format(self.animalList[i],self.sounds[i]))


    def refactNoises(self):
        for i in range(len(self.animalList)):
            yield self.animalList[i],self.sounds[i]
            print('-'*30)
            print("The noise that ",self.animalList[i],self.sounds[i])
            print('-' * 30)


x=['duck','rabbit','tiger','seagull','cat','shark']
y= ['Quack','Mak','RAWWR','GIU GIU',"meow",'jaw']


firstObject=Animals(x,y)
firstObject.noises()

z=firstObject.refactNoises()
next(z)
next(z)
next(z)
next(z)