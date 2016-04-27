class CustomSet:
        def __init__(self, setList):
                '''
                Description: creates an object of CustomSet type
                PreConditions: setList must be a list
                PostConditions: makes attributes private
                '''
                aList = []
                for num in setList:
                    if num not in aList:
                        aList.append(num)
                self._SetElements = aList

        def __str__(self):
                '''
                Description: returns a string of data from CustomSet class
                PreConditions: setList is a list
                PostConditions: makes a string based on private data
                '''
                tmp = ''
                tmp += '{'
                for num in self._SetElements:
                    if num == self._SetElements[len(self._SetElements)-1]:
                        tmp += str(num)
                    else:
                        tmp += str(num) + ','
                tmp += '}'
                return tmp
        
        def __add__(self, other):
                '''
                Description: adds to CustomSet objects together and returns it
                PreConditions: self and other must both be CustomSet objects
                PostConditions: creates a new CustomSet object
                '''
                aList = self._SetElements + other._SetElements
                return CustomSet(aList)   

    




