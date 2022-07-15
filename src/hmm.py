from functools import lru_cache


# "F" = fair
# "R" = rigged
# "H" = heads
# "T" = tails

probabilities = {"F":{"H":0.5, "T":0.5}, "R":{"H":0.75, "T":0.25}}
p_switch = 1/19

@lru_cache(maxsize=256)
def rec_markov(sequ, pos=0, state=None):
    if pos >= len(sequ): return ("", 1)
    if pos == 0 and state==None: 
        a = rec_markov(sequ, pos, "F")
        b = rec_markov(sequ, pos, "R")
        return a if a[1] > b[1] else b

    p_coin = probabilities[state][sequ[pos]]
    if pos == len(sequ)-1:
        return (state, p_coin)

    a = rec_markov(sequ, pos+1, "F")
    b = rec_markov(sequ, pos+1, "R")
    
    
    
    if state == "F":
        if (a[1] > b[1]*p_switch):
            return (state+a[0], a[1]*p_coin)
        else:
            return (state+b[0], b[1]*p_switch*p_coin)
    elif state == "R":
        if (a[1]*p_switch > b[1]):
            return (state+a[0], a[1]*p_switch*p_coin)
        else:
            return (state+b[0], b[1]*p_coin)


def bottom_up_markov(sequ):
    n = len(sequ)
    ansr = "R"
    ansf = "F"
    mem = {"R": [probabilities["R"][sequ[i]] for i in range(n)], "F": [probabilities["F"][sequ[i]] for i in range(n)]}
    for i in range(1, n):
        if mem["R"][i-1] > mem["F"][i-1]*p_switch:
            ar = ansr+"R"
            mem["R"][i] *= mem["R"][i-1]
        else:
            ar = ansf+"R"
            mem["R"][i] *= mem["F"][i-1]*p_switch
        
        if mem["F"][i-1] > mem["R"][i-1]*p_switch:
            af = ansf+"F"
            mem["F"][i] *= mem["F"][i-1]
        else:
            af = ansr+"F"
            mem["F"][i] *= mem["R"][i-1]*p_switch
        ansf = af
        ansr = ar
    
    return (ansr, mem["R"][-1]) if mem["R"][-1] > mem["F"][-1] else (ansf, mem["F"][-1])


sequ = "HHHHHTTTTT"

print (bottom_up_markov(sequ))







