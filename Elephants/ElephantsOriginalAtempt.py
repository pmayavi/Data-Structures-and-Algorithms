# this code was adapted from 
# https://github.com/secnot/uva-onlinejudge-solutions/blob/master/10131%20-%20Is%20Bigger%20Smarter%3F/main.py
from sys import stdin, stdout


def readnum():
    return list(map(int,stdin.readline().split()))


def readcase():
    ele = [] 
    line = stdin.readline().strip().split()
    index = 1
    while len(line) > 0:
        ele.append((int(line[0]),int(line[1]),index))
        index +=1 
        line = stdin.readline().strip().split()
    return ele


def find_sequence(elephants):
    """Find longest sequence of elephants satisfying the problem condition"""
    # Sort descending weight, and increasing iq
    seq = sorted(elephants, key=lambda y: (y[0], -y[1]), reverse=True)

    # seq_len contains the length for longest sequence reachable from each position
    seq_len = [1]*len(seq)

    # seq_nxt 'points' to the position of the next element in the largest sequence
    seq_nxt = [n for n, _ in enumerate(seq)]

    # Iterate from the end to the start of the list building the longest sequences
    for c in range(1, len(seq)):
        current_weight, current_iq, index = seq[c] # Current elephant

        for j in range(c-1, -1, -1):
            weight, iq, index = seq[j]
            # Check iq is in of sequence
            if iq >= current_iq:
                continue
            # Same weight, if the sequence is larger than current copy it
            if current_weight == weight:
                # If the sequence is larger than current copy it
                if seq_len[j] > seq_len[c]:
                    seq_len[c] = seq_len[j]
                    seq_nxt[c] = seq_nxt[j]
            # Smaller weight, add sequence to current if it is longer
            else:
                if seq_len[j] >= seq_len[c]:
                    seq_len[c] = seq_len[j]+1
                    seq_nxt[c] = j

    # Find the starting position of the longest sequence
    lenght, start = max((s, n) for n,s in enumerate(seq_len))
    stdout.write(str(lenght))
    # Reconstruct sequence (using ordered seq indexes)
    longest = [start]
    while seq_nxt[longest[-1]]!=longest[-1]:
        longest.append(seq_nxt[longest[-1]])

    # Substitute sequence positions by original elephant numbers
    return [seq[e][2] for e in longest]


if __name__ == '__main__':
    elephants = readcase()
    seq = find_sequence(elephants)
    for e in seq:
        stdout.write(str(e))