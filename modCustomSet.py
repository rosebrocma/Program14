class CustomSet:
        def __init__(self, setList):
                '''
                Description: (Matthew R. wrote this) creates an object of CustomSet type
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
                Description: (Matthew R. wrote this) returns a string of data from CustomSet class
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
                Description: (Matthew R. wrote this) adds to CustomSet objects together and returns it
                PreConditions: self and other must both be CustomSet objects
                PostConditions: creates a new CustomSet object
                '''
                aList = self._SetElements + other._SetElements
                return CustomSet(aList)   
        
         def __rand__(self, other):
                '''Descriptioin - (Ryan wrote this method)takes the two sets and returns a new set with the union of the two
                PreCondition - self and other must both be of CustomSet objects
                PostCondition - a new CustomSet object is created'''
                newSet = []
                aList = self._SetElements
                for ele in aList:
                    if ele in other._SetElements:
                        newSet.append(ele)
                return CustomSet(newSet)


        def __sub__(self, other):
                '''Description - (Ryan wrote this method) takes the difference between two sets and returns the result
                PreConditon - self and other must both be of the type CustomSet
                PostCondition - a new CustomSet is created'''
                aList = self._SetElements
                newSet = []
                for ele in aList:
                    if ele not in other._SetElements:
                        newSet.append(ele)
                return CustomSet(newSet)
        
        
        def __contains__(self, num):
                '''Description - (Ryan wrote this method) checks to see if a given number is in the CustomSet
                PreCondition - self must be of type CustomSet
                PostCondition - a correct statement is given according to the truth of the statment'''
                return num in self._SetElements


    




