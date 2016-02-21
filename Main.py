import win32com.client as win32
import datetime
import sys
import os
from DT228B_LIB.MyEncryptor import MyEncryptor
from DT228B_LIB.BruteForcer import BruteForcer


def conclusion(val1,val2):
    print "----------------------------------------------"
    if val1 == val2:
        print "Conclusion :"
        print "Both before and after hash values are the same "
    else:
        print "Conclusion :"
        print "Both before and after hash values are the same "


def start():
    fileToEncode = "C:\Users\Terry\PycharmProjects\lab3\DT228B_LAB3\MDF-SF1.docx"
    wordlist = r"C:\Users\Terry\PycharmProjects\lab3\DT228B_LAB3\4digits.txt"
    print "Getting hash of " + fileToEncode
    originalHash = MyEncryptor.sha1Encode(fileToEncode)
    print "The Sha1Encode value of the file is  : " ,originalHash

    print "Attempting to crack file " + fileToEncode
    print "Starting Brute force : ", datetime.datetime.now().time()
    result = BruteForcer.crackFile(wordlist,fileToEncode)

    print "Password is " ,result
    print "Finished Brute force : ", datetime.datetime.now().time()
    print "---------------------------"
    print "Hashing file again"
    print "Starting hash again : ", datetime.datetime.now().time()
    print "Getting hash of " + fileToEncode
    secondHashValue = MyEncryptor.sha1Encode(fileToEncode)
    print "The Sha1Encode value of the file is  : " ,secondHashValue
    print "Finished Hash : ", datetime.datetime.now().time()

    print "Generating results"
    conclusion(originalHash,secondHashValue)

start()
