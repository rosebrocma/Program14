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
        
  
    def __le__(self,other):
        """
        Descriptions: Spencer(Spendy33)made this. Makes it able to so we can see objects of type CustomSet
        are a subset one another.
        PreConditions: Objects must be of type CustomSet
        PostConditions: None
        """
        ct = 0
        numsInOther=0
        while ct < len(self._SetElements):
            for self._SetElements[ct] in self._SetElements:
                if self._SetElements[ct] in other._SetElements:
                    numsInOther+=1
                    ct+=1
                elif self._SetElements[ct] not in other._SetElements:
                    numsInOther+=0
                    ct+=1
            if numsInOther == len(self._SetElements):
                return  True
            else:
                return False

    def __ge__(self,other):
        """
        Descriptions:Spencer(Spendy33)made this. Makes it able to so we can see objects of type CustomSet
        are a superset of one another.
        PreConditions: Objects must be of type CustomSet
        PostConditions: None
        """
        ct = 0
        numsInOther=0
        while ct < len(other._SetElements):
            for other._SetElements[ct] in other._SetElements:
                if other._SetElements[ct] in self._SetElements:
                    numsInOther+=1
                    ct+=1
                elif other._SetElements[ct] not in self._SetElements:
                    numsInOther+=0
                    ct+=1
            if numsInOther == len(other._SetElements):
                return  True
            else:
                return False

    def __len__(self):
        """
        Description:Spencer(Spendy33)made this.Makes it able to use len on objects of type CustomSet.
        PreConditions: None
        PostConditions: None
        """
        return len(self._SetElements)
    




