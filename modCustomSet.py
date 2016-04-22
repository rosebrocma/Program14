class CustomSet:
def __init__(self, setList):
        ''''''
        aList = []
        for num in setList:
            if num not in aList:
                aList.append(num)
        self._SetElements = aList

    def __str__(self):
        ''''''
        tmp = ''
        
        tmp += '{'
        for num in self._SetList:
            tmp += str(num) + ','
        tmp += '}'
        return tmp





