import sys


def dict(s):
    if s in diction:
        return True
    return False


def b_up(s):
    # Initialize lists to be used
    splittable_at = [False] * (len(s) + 1)  # To determine if the previous substrings also splittable
    split_index = [0] * (len(s) + 1)  # To determine the indexes that we can split

    n = len(s)
    possible = False

    # Base Case
    splittable_at[0] = True

    # iterate from i = 1 to length of the word
    for i in range(n + 1):
        # iterate the substring of word[:i] from j = 0 to i
        for j in range(0, i):
            # if the substring is in dictionary and previous substring is splittable
            if (dict(s[j:i])) and splittable_at[j]:
                splittable_at[i] = True
                split_index[i] = j
                if i == n:
                    possible = True

    if not possible:
        return False
    elif possible:
        i = n
        while i != 0:
            s = s[:split_index[i]] + " " + s[split_index[i]:]
            i = split_index[i]
        ans.append(s.strip())
        return True


if __name__ == '__main__':

    # add dictionary to diction
    diction = set()
    dictionary = open("diction10k.txt", "r")
    for word in dictionary:
        diction.add(word.strip())
    dictionary.close()

    # read stdin
    phrase_num = int(sys.stdin.readline())
    samples = []
    for line in sys.stdin:
        samples.append(line.rstrip())

    # run the code for every phrase
    for i in range(phrase_num):
        print(f"phrase number: {i + 1}")
        print(samples[i] + "\n")

        # iterative
        print(f"iterative attempt:")
        ans = []
        if b_up(samples[i]):
            print(f"YES, can be split")
            ans.reverse()
            for j in ans:
                print(j, end=' ')
            print("\n\n")
        else:
            print(f"NO, cannot be split")
            print("\n")
