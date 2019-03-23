import random
import numpy as np


dataset = [0,3,5,7.8,9,12,13.8]

#print(random.choice(dataset))

def find_interval(x,partition):
    for i in range(len(partition)):
        if x < partition[i]:
            return i-1
    return -1

# for i in [-1.3,0,0.1,3.2,5,6.2,7.8,10.2,16,16.5]:
#     print(find_interval(i,dataset),end=", ")

def find_interval_new(x,
                  partition,
                  endpoints=True):
    """ find_interval -> i
        If endpoints is True, "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise

        If endpoints is False, "i" will be the smallest index
        for which applies x < partition[i]. If no such index exists
        "i" will be set to len(partition)
    """
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i - 1 if endpoints else i
    return -1 if endpoints else len(partition)

def weighted_choice(sequence,
                    weights,
                    secure=False):
    """
    weighted_choice selects a random element of
    the sequence according to the list of weights
    """

    if secure:
        crypto = random.SystemRandom()
        x = crypto.random()
    else:
        x = np.random.random()
    #print(x)
    cum_weights = [0] + list(np.cumsum(weights))
    #print(cum_weights)
    index = find_interval_new(x, cum_weights)
    return sequence[index]

n = []
counter = []
for i in range(10000):
    n.append(weighted_choice([1,2,3,4,5,6],[1/12,1/6,1/6,1/6,1/6,3/12]))

for i in range(1,7):
    count = n.count(i)/len(n)
    counter.append(count)
print(counter)

professions = ['Engineer','Doctor','Journalist','Scientist']
probabilities = [0.4,0.3,0.2,0.1]
d = []
counter_new = []
for i in range(10000):
    d.append(np.random.choice(professions,p=probabilities))

for i in professions:
    count = d.count(i)/len(d)
    counter_new.append(count)
print(counter_new)





