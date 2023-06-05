import math
import scipy

# lProb = numSucc / numProve

def CalcoloEntropiaRelativa(lProb, numProve):
    
    numSucc = []
    
    for i in range(len(lProb)):
        
        num = (lProb[i] * numProve)
        
        numSucc.append(num)
        
    sumSucc = sum(numSucc)
    
    prob = []
    
    for i in range(len(lProb)):
        
        prob.append(lProb[i] / sumSucc)
        
        
    entropia = scipy.stats.entropy(prob)

    max_entropia = math.log(len(lProb))

    entropia_relativa = entropia / max_entropia

    print("\n Entropia: " + str(entropia)+ "\n Entropia relativa: " + str(entropia_relativa))



    


