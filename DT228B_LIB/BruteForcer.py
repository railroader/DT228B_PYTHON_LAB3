import win32com.client as win32

class BruteForcer():
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

    def crackFile(self):
        word = win32.Dispatch("Word.Application")
        filename = self._fileToCrack
        password_file = open(self._wordList, 'r')
        passwords = password_file.readlines()
        password_file.close()
        passwords = [item.rstrip('\n') for item in passwords]

        for password in passwords:
            try:
                doc = word.Documents.Open(filename,False,True,None,password)
                doc.Close()
                return str(password)
            except Exception as error:
                pass
        return ""

    @staticmethod
    def crackFile(wordlist,WordDocToCrack):
        word = win32.Dispatch("Word.Application")
        filename = WordDocToCrack
        password_file = open(wordlist, 'r')
        passwords = password_file.readlines()
        password_file.close()
        passwords = [item.rstrip('\n') for item in passwords]

        for password in passwords:
            try:
                doc = word.Documents.Open(filename,False,True,None,password)
                doc.Close()
                return str(password)
            except Exception as error:
                pass
        return ""