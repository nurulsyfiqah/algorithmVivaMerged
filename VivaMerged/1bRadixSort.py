def radixSort(arr):
    max1 = max(arr) 
    exp = 1
    while (int(max1/exp)) > 0:
        if(exp==1):
            print("One's digit > ", countingSort(arr,exp))
            exp *= 10
        elif(exp==10):
            print("Ten's digit > ", countingSort(arr,exp))
            exp *= 10
        elif(exp==100):
            print("Hundred's Digit > ", countingSort(arr, exp))
            exp *= 10

def countingSort(arr, exp1):
    n = len(arr) 
    output = [0] * (n) 
    count = [0] * (10) 
 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
 
    for i in range(1,10): 
        count[i] += count[i-1] 
 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
    
    i = 0
    for i in range(0,n): 
        arr[i] = output[i]

    return arr

# Drive code
A = [ 84, 23, 62, 44, 16, 30, 95, 51]
print(A,"\n")
radixSort(A)

print("Final Output > ",end =" ")
for i  in range (len(A)):
    print(A[i],end =" ")
