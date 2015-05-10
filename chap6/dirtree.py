import os
def dirtree(folder, prefix=''):
     folderList = os.listdir(folder)
     for i in folderList:
        if os.path.isdir(os.path.join(folder,i)):
            if folderList.index(i) == len(folderList) - 1:
                 print prefix, '-- ', i, '/'
                 dirtree(os.path.join(folderlist,i), prefix + ' ')
            else:
                 print prefix, '|-- ', i, '/'
                 dirtree( os.path.join(folder,i), prefix + '| ')
        else:
             if folderList.index(i) == len(folderList) - 1:
                 print prefix, '--', i
             else:
                     print prefix, '|-- ', i
import sys
dirtree(sys.argv[1])

