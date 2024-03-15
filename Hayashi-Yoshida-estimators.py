import numpy as np
import random

def Interv(Length,Num):
    """
    Args:
    - Length (int): total length of you time series
    - Num (int): amount of wanted tuples
    """
    Ints = []
    while len(Ints)!=Num:
        first = random.sample(range(0, Length-10), 1)[0]
        second = random.sample(range(first, Length-10),1)[0]
        
        if first+second<Length:
            Ints.append((first,second))
    return Ints
    
def Increments(data,start,end):
    """
    Args:
    - data (numpy array): time series of one the random process
    - start (int): interval start
    - end (int): interval end
    """
    first = 0
    last = 0
    for i in range(end-start):
        if data[start+i]!=0:
            first+=data[start+i]
            break
    for i in range(end-start,-1,-1):
        if data[start+i]!=0:
            last+=data[start+i]
            break
            
    return last-first

def R1n(P1, P2, intervals, sigma1, sigma2):
    """
    Calculate correlation estimator R(1)_n.
    
    Args:
    - P1 (numpy array): First diffusion process.
    - P2 (numpy array): Second diffusion process.
    - intervals (list of tuples): List of tuples representing random intervals.
    - sigma1 (float): Standard deviation of process 1.
    - sigma2 (float): Standard deviation of process 2.
    
    Returns:
    - float: Correlation estimator R(1)_n.
    """
    n = len(intervals)
    sum_corr = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                interval1 = intervals[i]
                interval2 = intervals[j]
                intersect = min(interval1[1], interval2[1]) - max(interval1[0], interval2[0])
                if intersect > 0:
                    sum_corr += (Increments(P1,interval1[0],interval1[1])*Increments(P2,interval2[0],interval2[1])) / (sigma1 * sigma2)
    return sum_corr / n

#R1n(TS1,TS2,Interv(len(TS1),1000),.9,1.1) example

def R2n(P1, P2, intervals):
    """
    Calculate correlation estimator R(2)_n.
    
    Args:
    - P1 (numpy array): First diffusion process.
    - P2 (numpy array): Second diffusion process.
    - intervals (list of tuples): List of tuples representing random intervals.
    - sigma1_known (bool): Whether sigma1 is known or unknown.
    - sigma2_known (bool): Whether sigma2 is known or unknown.
    
    Returns:
    - float: Correlation estimator R(2)_n.
    """
    n = len(intervals)
    sum_num = 0
    sum_den1 = 0
    sum_den2 = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                interval1 = intervals[i]
                interval2 = intervals[j]
                intersect = min(interval1[1], interval2[1]) - max(interval1[0], interval2[0])
                if intersect > 0:
                    DP1 = Increments(P1,interval1[0],interval1[1])
                    DP2 = Increments(P2,interval2[0],interval2[1])
                    sum_num += DP1*DP2
                    sum_den1 += DP1**2
                    sum_den2 += DP2**2
    denominator = np.sqrt(sum_den1)*np.sqrt(sum_den2)
    return sum_num / denominator

#R2n(TS1,TS2,Interv(len(TS2),1000)) example




