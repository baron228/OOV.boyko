def MaxLenList(array, unique_array=[], final_array=[]):
    unique_array = list(set(map(lambda x : x[0], array)))
    final_array = sorted([max(filter(lambda x : i in x, array)) for i in unique_array])
    return [(i,len(i)) for i in final_array]
    
array = ["aa", "bbbb", "b", "ffffff", "fff", "wwwwwwww", "wwww"]      
print(MaxLenList(array))
