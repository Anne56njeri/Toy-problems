def search (collection,value):
    first_value = 0 
    last_value = len(collection)
    found = False
    sort= sorted(collection)
    while first_value <=last_value and not found:
        try:
            mid= (first_value + last_value)//2
            if sort[mid] == value:
                found = True 
            else:
                if value < sort[mid]:
                    last_value = mid -1 
                else:
                    first = mid + 1 
        except IndexError:
            return -1 
testList = [0,1,8,4,6,67]            
print (search(testList,4))