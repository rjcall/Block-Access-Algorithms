from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys

#  Robert Call
#  Operating Systems Theory - CS 3060
#  Assignment 6 - Block Access Algorithms


'''
Promise of Originality
I promise that this source code file has, in its entirety, been
written by myself and by no other person or persons. If at any time an
exact copy of this source code is found to be used by another person in
this term, I understand that both myself and the student that submitted
the copy will receive a zero on this assignment.
'''


#  First Come First Serve
def fcfs(nums):

    s = [x[0] - x[1] for x in list(zip(nums[:-1],nums[1:]))]
    diffs = []

    for x in s:
        if x < 0:
            x *=-1
        diffs.append(x)

    return sum(diffs)


#  Shortest Seek Time First
def sstf(nums):

    q = [x for x in nums]
    s = q[0]
    q.remove(q[0])

    ttls = []

    while len(q) > 0:

        deltas = []
        delta = [x - s for x in q]

        for x in delta:
            if x < 0:
                x *= -1

            deltas.append(x)

        ttls.append(min(deltas))
        s = q[deltas.index(min(deltas))]
        q.remove(s)

    return sum(ttls)


#  Non-circular LOOK
def look(q):
    s = q[0]
    q = sorted(q)

    lower = q[q.index(s) - 1::-1]
    upper = q[q.index(s):]

    ordered = upper + lower

    return fcfs(ordered)


#  Circular Look
def c_look(q):
    s = q[0]
    q = sorted(q)

    lower = q[:q.index(s)]
    upper = q[q.index(s):]

    ordered = upper + lower

    return fcfs(ordered)


def main():
    print("Assignment 6: Block Access Algorithm\nBy: Robert Call")
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r") as f:
                nums = f.read()
        except:
            print("\nError with file.\nUse: python assn6.py <filename.txt>\n")
            return -1

        nums = [int(x) for x in nums.split('\n')[:-1]]
        uno = fcfs(nums)
        dos = sstf(nums)
        tres = look(nums)
        quatro = c_look(nums)
        print("\nFCFS Total Seek: %d\nSSTF Total Seek: %d\nLOOK Total Seek: %d\nC-LOOK Total Seek: %d\n" % (uno, dos, tres, quatro))
    else:
        print("\nERROR: No list file provided.\nUse: python assn6.py <filename.txt>\n")



if __name__ == "__main__":
    # execute only if run as a script
    main()