#!/usr/bin/python

import crypt
import sys

def testPass(cryptPass, dic):
    salt = cryptPass[0:2]
    dictFile = open(dic, 'r')

    for word in dictFile.readlines():
        word = word.strip('\n')
        ced = crypt.crypt(word, salt)
        if (ced == cryptPass):
            print "[+] Found Password: " + word + "(" + cryptPass + ")\n"
            return

    print "[-] Password Not Found.\n"
    return


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Usage: ./crypt_crack.py "$CRYPT" "$DICT_FILE"'
    else:
        testPass(sys.argv[1], sys.argv[2])

# Usage: 
# ./decrypt.py GGvxb.e7YgnIg /usr/share/dict/words
