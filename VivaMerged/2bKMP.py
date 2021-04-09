text= "algorithmisfun" 
pattern= "fun" 
premap = [] 
catch = []  #Catch array not necessary. Only for presenting purposes 
n = len(text) 
m= len(pattern)
i = 0 
j = 0 
while(i < m): 
 
    if(i == 0): 
        premap.append(0) 
        catch.append(pattern[i]) 
        i += 1 
 
    else: 
 
        if(pattern[i] == pattern[j]): 
            premap.append(j+1) 
            catch.append(pattern[i]) 
            j += 1 
            i += 1 
 
        else: 
 
            if(j == 0): 
                premap.append(0) 
                catch.append(pattern[i]) 
                i += 1 
                j += 1 
 
            else: 
                j = premap[j-1] 
                continue 
 
    print("{}, {}".format(catch,premap))    #To show the creation of premap 
 
a = 0 
b = 0 
detected = False 
 
while(a < n and detected == False): 
 
    print(text[a]) 
 
    if(text[a] == pattern[b]): 
        a += 1 
        b += 1 

        if(b == (m)): 
            detected = True #System stops once the earliest instance of word is found 
            continue 
 
    else: 
        if(b == 0): 
            a += 1 
 
        else: 
            b = premap[b - 1] 
 
if(detected == True): 
    print("Pattern is found in the string at index number {}".format(a - m )) 
 
else: 
    print("Not found...") 
