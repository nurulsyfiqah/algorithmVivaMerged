def Rabin_Karp (pattern,text, q,d): 

    P = len(pattern) 
    T = len(text) 
    i=0 
    j=0 
    hashP = 0 
    hashT = 0 
    hash = 1 
    mark = False 

    for i in range(P-1): 
         hash = (hash*d) % q 

    for i in range(P): 
        hashP = (d*hashP+ord(pattern[i])) % q 
        hashT = (d*hashT+ord(text[i])) % q 

    for i in range(T-P+1): 
        if hashT == hashP: 
            for j in range(P):  
                if (text[i + j] != pattern[j]): 
                    break 
                else: 
                    j+=1 

                if j==P: 
                    print ('Rabin-Karp Algorithm: Pattern found at index '+str(i)) 
                    mark = True              


        if i < T-P:  
            hashT = (d*( hashT- ord(text[i]) * hash) + ord(text[i+P])) % q 

            if hashT<0: 
                hashT = hashT + q     

            if mark is False: 
                print ('Rabin-Karp Algorithm: Pattern not found') 

#Drive code 
text="algorithmisfun" 
pattern="fun" 
q=11 #prime number 
d=256 #number of characters 
Rabin_Karp(pattern,text,q,d)