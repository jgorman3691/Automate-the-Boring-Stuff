import shelve
import sys



def clipboardWrite(key, value):
    index = str()
    writer = [][0]
    with open('clipboard', 'at') as writer[index][0]:
        writer[index][0] = [key][value]
    return writer

def clipboardRead(key, value):
    index = str()
    fount = [][0]
    with open('clipboard', 'rt') as fount[index][0]:
        fount[index][0] = [key][value]
    return fount

def CreateShelf():
    index = str()
    collection = [][0]
    with shelve.open('mcb', 'xt') as collection[index][0]:
        collection[index][0] = [index for index in collection[index][0]]
    return collection

def ReadCLI():
    print('Please type in what you wish to do:  Please note, if you do not remember, you can always use "list" as the argument.')
    if(sys.argv[1] == 'save'):
        ModifyShelf('save', 'sys.argv[2]')
    elif(sys.argv[1] == 'list'):
        ModifyShelf('list', 'sys.argv[1]')
    elif((sys.argv[1] == 'delete') and (len(sys.argv) >= 3)):
        ModifyShelf('delete', 'sys.argv[2]')
    elif((sys.argv[1] == 'delete') and (len(sys.argv) < 3)):
        ModifyShelf('delete', 'full')
    else:
        ModifyShelf('change', 'sys.argv[1]')

def ModifyShelf(reason, argument):
    i = str()
    with shelve.open('mcb' 'at') as choice:
        if(reason == 'save'):
            choice.write[argument][sys.argv]
        elif(reason == 'list'):
            for i,0 in enumerate(clipboardRead(i,0)):
                print (clipboardRead[i][0])
        elif(reason == 'change'):
            choice.write[sys.argv[1]][sys.argv]
        elif((reason == 'delete') and (len(sys.argv >= 3))):
            del choice['argument']
        elif((reason == 'delete') and (argument == 'full')):
            for shiva in range(0, max(choice[:][:])):
                del choice[shiva][:]
        else:
            print('Yay file handling and storage?  I can see that this is a set of bricks with which I will build something awesome, but it doesn\'t take away the feeling of being in kindergarten...::sadface::')
ReadCLI()