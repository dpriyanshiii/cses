#input between 1 to 1000000 char that are ACGT
#output is a number.

dna = input()

if (1 <=  len(dna) and len(dna) <= 1000000):
    if (len(dna) == 1):
        print(1)
    else:
        lmaxis = 0
        maxis = 0
        for i in range(len(dna)):
            #hold = dna[i]
            for j in range(len(dna)-i):
                if (dna[i] == dna[i+j]):
                    lmaxis += 1
                else:
                    if (lmaxis > maxis):
                        maxis = lmaxis
                        lmaxis = 0
        print(maxis)
            
                    
                    

