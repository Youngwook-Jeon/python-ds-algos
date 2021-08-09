def construct_pi(pattern):
    pi_table = [0] * len(pattern)
    prefix_counter = 0
    i = 1

    # O(M) linear running time
    while (i < len(pattern)):
        if pattern[i] == pattern[prefix_counter]:
            prefix_counter += 1
            pi_table[i] = prefix_counter
            i += 1
        else:
            if prefix_counter != 0:
                prefix_counter = pi_table[prefix_counter - 1]
            else:
                pi_table[i] = 0
                i = i + 1
    return pi_table

def search(text, pattern):
    pi_table = construct_pi(pattern)
    i = 0
    j = 0

    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print("pattern found at index %s" % (i - j))
            # reinitialize the j index to be able to find more pattern matches
            j = pi_table[j - 1]
        # if there is a mismatch
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = pi_table[j - 1]
            else:
                i += 1

if __name__ == "__main__":
    search('this is a text test also another test', 'test')