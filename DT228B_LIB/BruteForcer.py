import win32com.client as win32


#class to brute force a password protected wordfile
class BruteForcer():
    #public private properties below

    _wordList = ""
    _fileToCrack = ""

    @property
    def wordList(selfself):
        return BruteForcer._prop

    @wordList.setter
    def wordList(self, val):
        BruteForcer._wordList = val

    @property
    def fileToCrac(selfself):
        return BruteForcer._fileToCrac

    @fileToCrac.setter
    def fileToCrac(self, val):
        BruteForcer._fileToCrac = val


    # CLASS CONSTRUCTOR
    def __init__(self):
        pass


    #method to crack the pin
    def crackFile(self):
        word = win32.Dispatch("Word.Application")#call the win32.Dispatch with looks like a static method returning an object
        '''
        open wordlist and read the values into a object of type listOf<string>
        and the strip out the \n
        '''
        password_file = open(self._wordList, 'r')
        passwords = password_file.readlines()
        password_file.close()
        passwords = [item.rstrip('\n') for item in passwords]

        '''
        iterate through the list and pass the current value in the password list to the open method of the word doc
        if the document opens then return the password
        '''

        for password in passwords:
            try:
                doc = word.Documents.Open(self._fileToCrack,False,True,None,password)
                doc.Close()
                return str(password)
            except Exception as error:
                pass
        return ""


    #Decided to make the method static as i felt the object does not need to be instantiated
    @staticmethod
    def crackFile(wordlist,WordDocToCrack):
        word = win32.Dispatch("Word.Application") #call the win32.Dispatch with looks like a static method returning an object
        '''
        open wordlist and read the values into a object of type listOf<string>
        and the strip out the \n
        '''
        password_file = open(wordlist, 'r')
        passwords = password_file.readlines()
        password_file.close()
        passwords = [item.rstrip('\n') for item in passwords]

        '''
        iterate through the list and pass the current value in the password list to the open method of the word doc
        if the document opens then return the password
        '''

        for password in passwords:
            try:
                doc = word.Documents.Open(WordDocToCrack,False,True,None,password)
                doc.Close()
                return str(password)
            except Exception as error:
                pass
        return ""