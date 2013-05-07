#!/usr/bin/python

import sys
import itertools

def f(S, l):
    for j in ("".join(i) for i in (itertools.combinations_with_replacement(S, l))):
        print j

if __name__ == '__main__':
    alpha = ""
    if len(sys.argv) != 3:
        print "Usage: " + sys.argv[0] + " aAdx 10"
        sys.exit(1)
    else:
        if 'a' in sys.argv[1]: alpha += "abcdefghijklmnopqrstuvwxyz"
        if 'A' in sys.argv[1]: alpha += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if 'd' in sys.argv[1]: alpha += "0123456789"
        if 'x' in sys.argv[1]: alpha += """\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ """

        f(alpha, int(sys.argv[2]))

