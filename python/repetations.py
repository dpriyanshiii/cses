#input between 1 to 1000000 char that are ACGT
#output is a number.

dna = input()
dnaa = dna + "x"

if (1 <=  len(dna) and len(dna) <= 1000000):
    maxis = 1
    store = []
    if (len(dna) > 1):
        #method 1 for finding lenght of all substrings
        for i in range(len(dna)):
            if (dnaa[i] == dnaa[i+1]):
                maxis += 1
            else:
                store.append(maxis)
                maxis = 1
        #print(store)

        #find max in store
        finalmax = 1
        for i in store:
            if (i > finalmax):
                finalmax = i
        print(finalmax)
    else:
        print(1)


#note to self: if the ps asked for any kind of input (instead of specified char ones)
#repetations we would have split the substrings, stored them,
#then found each's length then find max            

