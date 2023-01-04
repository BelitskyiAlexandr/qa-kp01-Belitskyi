from binary_file import BinaryFile
from directory import Directory
from bufferFile import BufferFile
from logtextfile import LogTextFile

home = Directory("home")
log = LogTextFile()
log.move(home)
binary = BinaryFile(home, log, "Binn")
binaryf = BinaryFile(home, log, "Bins")
bufferfile = BufferFile(5, home, log, "")
nested_dir = Directory("nested_dir")
nested_dir.move_repository(home)

while True:
    command = input('Enter command: ')
    command = command.split()
    if command[0] == 'exit':
        break


    # directory
    elif command[0] == 'mkdir':     # make
        print("okmkdir")
    elif command[0] == 'mvdir':  # move
        print("okmvdir")
    elif command[0] == 'rddir':  # read
        print("okrddir")
    elif command[0] == 'deldir':  # delete
        print("okdeldir")


    # binary
    elif command[0] == 'mkbin':     # make
        print("okmkbin")
    elif command[0] == 'mvbin':     # move
        print("okmvbin")
    elif command[0] == 'rdbin':     # read
        print("okrdbin")
    elif command[0] == 'delbin':     # delete
        print("okdelbin")


    # buff
    elif command[0] == 'mkbuf':     # make
        print("okmkbuf")
    elif command[0] == 'appqu':     # add item
        print("okappqubuf")
    elif command[0] == 'popqu':     # pop item
        print("okpopbuf")
    elif command[0] == 'mvbuf':     # move
        print("okmvbuf")
    elif command[0] == 'rdbuf':     # read
        print("okrdbuf")
    elif command[0] == 'delbuf':     # delete
        print("okdelbuf")


    # log
    elif command[0] == 'mklog':  # make
        print("oklgmk")
    elif command[0] == 'mvlog':  # move
        print("okmvlg")
    elif command[0] == 'rdlog':  # read
        print("okrdlg")
    elif command[0] == 'dellog':  # delete
        print("okdellg")

    #ex
    else: print("Unknown command")