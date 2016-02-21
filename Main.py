import win32com.client as win32 #download at https://sourceforge.net/projects/pywin32/files/
import datetime
import sys
import os
from DT228B_LIB.MyEncryptor import MyEncryptor #import the encryptor so we can use it here
from DT228B_LIB.BruteForcer import BruteForcer #import the bruteforcer so we can use it here


def conclusion(val1,val2):
    print "----------------------------------------------"
    if val1 == val2:
        print "Conclusion :"
        print "Both before and after hash values are the same "
    else:
        print "Conclusion :"
        print "Both before and after hash values are not the same "

#Function to kick it all off
def start():
    fileToEncode = "C:\Users\Terry\PycharmProjects\lab3\DT228B_LAB3\MDF-SF1.docx" #File the we want to crack
    wordlist = r"C:\Users\Terry\PycharmProjects\lab3\DT228B_LAB3\4digits.txt" #wordlist with all the passwords
    print "Getting hash of " + fileToEncode
    originalHash = MyEncryptor.sha1Encode(fileToEncode) #get the sha1 hash of the file
    print "The Sha1Encode value of the file is  : " ,originalHash

    print "Attempting to crack file " + fileToEncode
    print "Starting Brute force : ", datetime.datetime.now().time() #print current time
    result = BruteForcer.crackFile(wordlist,fileToEncode) #get the pin

    print "Password is " ,result #print the password
    print "Finished Brute force : ", datetime.datetime.now().time() #print the current time
    print "---------------------------"
    print "Hashing file again"
    print "Starting hash again : ", datetime.datetime.now().time()
    print "Getting hash of " + fileToEncode
    secondHashValue = MyEncryptor.sha1Encode(fileToEncode) #get the sha1 hash of the file
    print "The Sha1Encode value of the file is  : " ,secondHashValue
    print "Finished Hash : ", datetime.datetime.now().time()

    print "Generating results"
    conclusion(originalHash,secondHashValue) #call conclusion function to compair the two hashes

start() #call the start function
