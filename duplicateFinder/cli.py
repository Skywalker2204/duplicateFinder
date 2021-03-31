"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
====         ===  ==       ==  ==           |      M ontan
||\\        //||  ||       ||  ||           |      U niversitaet
|| \\      // ||  ||       ||  ||           |      L eoben
||  \\    //  ||  ||       ||  ||           |
||   \\  //   ||  ||       ||  ||           |      Institute for 
||    \\//    ||  ||       ||  ||           |      polymer processing
||            ||  ||       ||  ||           |
||            ||   =========    ==========  |      Author:    Sykwalker
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
import os, sys
import duplicateFinder

class cli(object):
    
    def __init__(self):
        #define Variables
        self.__dFclass = duplicateFinder.duplicateFinder()
        print('Welcome!\nThis programm will find duplicate files,'\
              'hiding in the subfolders and have an equal content.\n'\
              'To start the programm insert the "-s" and the folder to start,'\
              'if none folder is supplied the execution folder is taken as starting point')
        pass
    
    def _printInfo(self):
        info = 'Following commands are avaliable:\n'
        functions = ['-s [directory]\tfind duplicate files in subfolders starting from directory.\n'\
                     'If directory is empty the execution directory is used.\n']
        functions.append('-q\twill quit the programm')
        
        for function in functions:
            info+=function
        print (info)
        
    def _findDuplicates(self, path):
        self.__dFclass.makeFileDict(path)
        self.__dFclass.findDupliactes()
        pass
        
    def _runApp(self):
        arg = input('Insert an operation:\n')
        if arg.startswith('-s'):
            self._findDuplicates(arg.split(' ')[-1])
        elif arg.startswith('-q'):
            self.__exit__()
        else:
            print('Invalid command:\t' + arg)
            self._printInfo()
    
    def __exit__(self):
        print('Programm closed!')
        sys.exit()
        pass
    
    def mainloop(self):
        for i in range(10):
            self._runApp()
        

if __name__ == '__main__':
    path = os.path.dirname(sys.argv[0])
    programm = cli()
    programm.mainloop()
    