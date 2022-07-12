alphabet = ["A", "C", "G", "T"]

intergenic_path = "./data/L1_intergenic.txt"

def enum_seq_of_sz(k):
    if k == 0: return [""]
    ans = []
    for x in alphabet:
        for word in enum(k-1):
            ans.append(x+word)
    return ans


def dfa_of_str(s):
    ans = []
    for i in range(len(s)):
        


print(enum_seq_of_sz(6))




