class CustomSet:
    def __init__(self, setList):
        ''''''
        aList = []
        for num in setList:
            if num not in aList:
                aList.append(num)
        self._SetList = aList

    def __str__(self):
        ''''''
        tmp = ''
        
        tmp += '{'
        for num in self._SetList:
            tmp += str(num) + ','
        tmp += '}'
        return tmp
    
    def __le__(self,other):
        """
        Descriptions: Makes it able to so we can see objects of type CustomSet
        are a subset one another.
        PreConditions: None
        PostConditions: None
        """
        ct = 0
        numsInOther=0
        while ct < len(self._SetList):
            for self._SetList[ct] in self._SetList:
                if self._SetList[ct] in other._SetList:
                    numsInOther+=1
                    ct+=1
                elif self._SetList[ct] not in other._SetList:
                    numsInOther+=0
                    ct+=1
            if numsInOther == len(self._SetList):
                return  True
            else:
                return False

    def __ge__(self,other):
        """
        Descriptions: Makes it able to so we can see objects of type CustomSet
        are a superset of one another.
        PreConditions: None
        PostConditions: None
        """
        ct = 0
        numsInOther=0
        while ct < len(other._SetList):
            for other._SetList[ct] in other._SetList:
                if other._SetList[ct] in self._SetList:
                    numsInOther+=1
                    ct+=1
                elif other._SetList[ct] not in self._SetList:
                    numsInOther+=0
                    ct+=1
            if numsInOther == len(other._SetList):
                return  True
            else:
                return False

    def __len__(self):
        """
        Description: Makes it able to use len on objects of type CustomSet.
        PreConditions: None
        PostConditions: None
        """
        return len(self._SetList)
