# THIRD PARTY LIBRARY FOR THE SHA3 IMPORT WAS TAKEN FROM https://pypi.python.org/pypi/pysha3/
# TO USE - FROM THE TERMINAL IN THE DOWNLOADED DIRECTORY TYPE
# python setup.py install
# THEN ADD A REFERENCE TO THE LIBRARY VIA EXTERNAL LIBRARIES IN JET BRAINS PYCHARM
import hashlib
import sha3
import os.path


# REUSABLE ENCRYPTION OBJECT THAT WILL HASH A FILE OR A STRING USING VARIOUS HASHING ALGORITHMS
# EACH METHOD DOES THE EXACT SAME THING USING A DIFFERENT TYPE OF ENCODING
class MyEncryptor():
    # CLASS CONSTRUCTOR
    def __init__(self):
        pass

    # METHOD TO SHA1 ENCODE OBJECT - WHICH CAN BE A FILE OR A STRING
    # FIRST CHECKS IF THE ARGUMENT IS A FILE
    # Also casts the value of the argument to a string
    # IF ITS NOT A FILE IT CHECKS IF ITS A STRING
    # IF IT IS A STRING THEN IT SHA1 ENCODES THE STRING
    # OTHERWISE IT TREATS THE ARGUMENT AS A FILE AND SHA1 ENCODES THE FILE

    def sha1Encode(self, text):
        if not os.path.isfile(str(text)):  # check if is a file
            if not text:  # check if its a string
                return "No String passed to method"
            else:
                m = hashlib.sha1()  # create new sha1 object
                m.update(text.encode('utf-8'))  # call udate method passing the 'utf-8' as an argument
                return (m.hexdigest())  # return the hash by calling hexdigest Method which returns the hash value
        else:
            BLOCKSIZE = 65536  # set the block size see :
            # http://www.dhillonblog.com/2014/07/understanding-io-request-block-size/
            hasher = hashlib.sha1()
            with open(text, 'rb') as afile:  # open file in read byte mode
                buf = afile.read(BLOCKSIZE)  # create a buffer of size blocksize call the file.read method
                while len(buf) > 0:  # while the length of the buffer is greater then a zero keep iterating
                    hasher.update(buf)  # append buffer to the current value in the hasher object
                    buf = afile.read(BLOCKSIZE)
            return (
            hasher.hexdigest())  # finally return the hash by calling hexdigest Method which returns the hash value

    def sha256Encode(self, text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha256()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha256()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())

    def sha512Encode(self, text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha512()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha512()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())

    def sha3_256Encode(self, text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha3_256()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha3_256()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())

    def sha3_512Encode(self, text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha3_512()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha3_512()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())

    @staticmethod
    def sha1Encode(text):
        if not os.path.isfile(str(text)):  # check if is a file
            if not text:  # check if its a string
                return "No String passed to method"
            else:
                m = hashlib.sha1()  # create new sha1 object
                m.update(text.encode('utf-8'))  # call udate method passing the 'utf-8' as an argument
                return (m.hexdigest())  # return the hash by calling hexdigest Method which returns the hash value
        else:
            BLOCKSIZE = 65536  # set the block size see :
            # http://www.dhillonblog.com/2014/07/understanding-io-request-block-size/
            hasher = hashlib.sha1()
            with open(text, 'rb') as afile:  # open file in read byte mode
                buf = afile.read(BLOCKSIZE)  # create a buffer of size blocksize call the file.read method
                while len(buf) > 0:  # while the length of the buffer is greater then a zero keep iterating
                    hasher.update(buf)  # append buffer to the current value in the hasher object
                    buf = afile.read(BLOCKSIZE)
            return (
            hasher.hexdigest())  # finally return the hash by calling hexdigest Method which returns the hash value
    @staticmethod
    def sha256Encode(text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha256()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha256()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())
    @staticmethod
    def sha512Encode(text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha512()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha512()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())
    @staticmethod
    def sha3_256Encode(text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha3_256()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha3_256()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())
    @staticmethod
    def sha3_512Encode(text):
        if not os.path.isfile(str(text)):
            if not text:
                return "No String passed to method"
            else:
                m = hashlib.sha3_512()
                m.update(text.encode('utf-8'))
                return (m.hexdigest())
        else:
            BLOCKSIZE = 65536
            hasher = hashlib.sha3_512()
            with open(text, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            return (hasher.hexdigest())