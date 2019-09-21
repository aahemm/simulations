import COA as coa
import SOA as soa
import FOA as foa
from copy import deepcopy,copy
from random import uniform

def run():
    MAX_FLOW = 0.25
    flow =  [315.392000, 405.504000, 360.448000, 331.776000, 237.568000,
             249.856000, 299.008000, 294.912000, 319.488000, 299.008000,
             266.240000, 229.376000, 241.664000, 212.992000, 192.512000,
             196.608000, 192.512000, 188.416000, 180.224000, 139.264000]
            
    maxf = max(flow)
    flow = [(f/maxf)*MAX_FLOW for f in flow]
    foa.f = copy(flow)
    soa.f = copy(flow)
    coa.f = copy(flow) 
    # running FOA...
    Y1,x1 = foa.foa()
    # running SOA...
    soa.NSP()
    Y2,x2 = soa.soa()
    # running COA...
    p,g = coa.NSP()
    Y3,x3 = coa.coa(g)
    
    Y = [[Y1,x1], [Y2,x2], [Y3,x3]]

    # finding the best assigment
    sum1 = controllerCounter(x1)
    sum2 = controllerCounter(x2)
    sum3 = controllerCounter(x3)
    optAssignment = argmin([sum1, sum2, sum3])
    return Y[optAssignment]


def controllerCounter(x):
    controllerSum = 0
    for item in x:
        if (item == 1):
            controllerSum += 1    
    return controllerSum        


def argmin(inputList):
     minValue = 100
     minIndex = -1
     i = 0
     for item in inputList:
          if (item < minValue):
               minValue = item
               minIndex = i
          i += 1           
     return minIndex  
