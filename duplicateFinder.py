import os
import sys
import hashlib
from collections import defaultdict
import csv

class duplicateFinder(object):
    """
    This class is written to finde Duplicates with the same content but do not
    finde files with the same names. 
    By input the operation on the file shall be executed
    Possilbe operations shall be delete, copies, moveing, and merging
    It is ment to be a cli programm
    """
    def __init__(self):
        #generate the dictonary with lists as values
        self.__md5Dict = defaultdict(list)
        self.__DuplicatesDict = defaultdict(list)
        
        
    def writeFile(self, path):
        """
        This functions save the duplicates in a file in a user friednly way.
        If an 'Duplicates.txt' already exists it will be removed.

        Parameters
        ----------
        path : String
            Contains the path of the execution directory in the command line

        Returns
        -------
        None.
        """        
        if os.path.isfile('Duplicates.txt'):
            os.remove('Duplicates.txt')
            
        with open('Duplicates.txt', 'a+') as file:
            file.write('Results of the found duplicate file with the same content: \n')
            
            for key, val in self.__DuplicatesDict.items():
                line = '\nFilename:\n' + key + '\n Found Duplicates:\n'
                for path in val:
                    line += path
                    line += '\n'       
                file.write(line)            
        pass
    
    
    def makeFileDict(self, path, followlinks=False):
        """
        This functions generates a dictonary with the files in the root
        directory and the corresponding subfolders. It stores the md5 checksum
        as key and the corresponding file path list as item. Duplicates are 
        present when the length of the list is greater than 1.

        Parameters
        ----------
        path : String
            Contains the root diretory to serach for files.

        Returns
        -------
        self.__md5Dict : Dictonary
            Contains the md5 checksum kez an the corresponding file paths

        """
        for root, dirs, files in os.walk(path, followlinks=followlinks): 
            for fn in files:
                filePath = os.path.join(root, fn) 
                self.__md5Dict[self.generate_md5(filePath)].append(filePath)
        return self.__md5Dict
    
    
    def generate_md5(self, fname, chunk_size=1024):
        """
        Function which takes a file name and returns md5 checksum of the file.
        Therefore, files with the same content but different names can also be
        found.
        
        Parameters
        ----------
        fname : String
            Contains the the file name and the path to the file.
        chunk_size : int
            Is the maximum number of bztes to be read and returned by
            the file read function.

        Returns
        -------
        hash.hexdigest() : String
            Rtuens the md5 checksum of the file.
        """
        hash = hashlib.md5()
        with open(fname, "rb") as f:
            # Read the 1st block of the file
            chunk = f.read(chunk_size)
            # Keep reading the file until the end and update hash
            while chunk:
                hash.update(chunk)
                chunk = f.read(chunk_size)

        # Return the hex checksum
        return hash.hexdigest()
    
    
    def findDupliactes(self):
        """
        This funciton shall finde the duplicates in the self.__md5Dict, 
        created in the function makeFileDict. Thus it retuns the files with 
        the same content. 

        Returns
        -------
        dictonary
            Returns a Dictonray sortetd by the first filename as key and
            the found duplicates ans their paths as list.

        """

        for key, val in self.__md5Dict.items():
            if len(val)>1:
                fn = os.path.split(val[0])[-1]
                self.__DuplicatesDict[fn] = val
                    #[os.path.split(path)[:-1] for path in val])
        
        if len(self.__DuplicatesDict.items()) != 0:
            print('Duplicates Found')
            
        return self.__DuplicatesDict
    
    
    def runApp(self, path):
        self.makeFileDict(path)
        self.findDupliactes()
        self.writeFile(path)
        #self.tree_printer(path)
        
        
                        
if __name__ == '__main__':
    path = os.path.dirname(sys.argv[0])
    dF = duplicateFinder()
    dF.runApp(path)