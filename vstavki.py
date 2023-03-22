def insertion_sort(N,array):
    from datetime import datetime
    import time
    start_time = datetime.now()

    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key 
    time.sleep(0.000000000000001)

    print(datetime.now() - start_time)
    vremya=(datetime.now() - start_time)
    return (array,str(vremya))   
'''array = [12, 11, 13, 5, 6]
N=5
print(insertion_sort(N,array))'''
