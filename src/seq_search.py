alphabet = ["A", "C", "G", "T"]
char2id = {"A":0, "C":1, "G":2, "T":3}

intergenic_path = "./data/L1_intergenic.txt"

def enum_seq_of_sz(k):
    if k == 0: return [""]
    ans = []
    for x in alphabet:
        for word in enum(k-1):
            ans.append(x+word)
    return ans


#Knth-Morris-Pratt substring search algorithm
def dfa_of_str(s):
    ss = [char2id[c] for c in s]
    dfa = [[0 for _ in range(len(alphabet))] for _ in range(len(ss)+1)]
    dfa[0][ss[0]] = 1
    ref_state = 0
    for i in range(1, len(ss)):
        for c in range(len(alphabet)):
            dfa[i][c] = dfa[ref_state][c]
        dfa[i][ss[i]] = i+1
        ref_state = dfa[ref_state][ss[i]]
    for c in range(len(alphabet)):
        dfa[len(ss)][c] = dfa[ref_state][c]
    return dfa


def count_seqs(seq, txt):
    ans = 0
    dfa = dfa_of_str(seq)
    print(dfa)
    st = 0
    end_st = len(seq)
    for c in txt:
        st = dfa[st][char2id[c]]
        if st == end_st:
            ans+=1
    return ans


print(count_seqs("AG", "AAGAAGA"))


#print(enum_seq_of_sz(6))




