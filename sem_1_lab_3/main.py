#!/usr/bin/env python3
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
        print("Exiting...")
        break

    # directory
    elif command[0] == 'mkdir':  # make
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: mkdir {name}")
            continue
        dir = Directory(command[1])
        dir.move_repository(home)
        print("okmkdir")

    elif command[0] == 'mvdir':  # move
        if len(command) != 3:
            print(
                "Incorrect number of args " + str(len(command)) + ", but need: mvdir {name_of_moving} {name_of_moveIn}")
            continue

        dirF = ""
        for item in home.list:
            if item.get_name() == command[1]:
                dirF = item
        if dirF == "":
            print("Directory " + str(command[1]) + " does not exist")
            continue

        dir = ""
        for item in home.list:
            if item.get_name() == command[2]:
                dir = item
        if dir == "":
            print("Directory " + str(command[2]) + " does not exist")
            continue

        home.delete_directory(dirF)
        dirF.move_repository(dir)

        print("okmvdir")

    elif command[0] == 'rddir':  # read
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: rddir {name}")
            continue

        if command[1] == "home":
            home.print_list()
            continue
        dirF = ""
        for item in home.list:
            if item.get_name() == command[1]:
                dirF = item

        if dirF == "":
            print("Directory " + str(command[1]) + " does not exist")
            continue
        dirF.print_list()
        print("okrddir")

    elif command[0] == 'deldir':  # delete
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: deldir {name}")
            continue
        dirF = ""
        for item in home.list:
            if item.get_name() == command[1]:
                dirF = item
        if dirF == "":
            print("Directory " + str(command[1]) + " does not exist")
            continue

        home.delete_directory(dirF)
        dirF.delete()
        print("okdeldir")


    # binary
    elif command[0] == 'mkbin':  # make
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: mkbin {name}")
            continue
        binaryfile = BinaryFile(home, log, command[1])
        print("okmkbin")

    elif command[0] == 'mvbin':  # move
        if len(command) != 3:
            print(
                "Incorrect number of args " + str(len(command)) + ", but need: mvbin {name_of_moving} {name_of_moveIn}")
            continue

        binF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".bin":
                binF = item
        if binF == "":
            print("BinaryFile " + str(command[1]) + " does not exist")
            continue

        dir = ""
        for item in home.list:
            if item.get_name() == command[2]:
                dir = item
        if dir == "":
            print("Directory " + str(command[2]) + " does not exist")
            continue

        binF.move(dir)

        print("okmvbin")

    elif command[0] == 'rdbin':  # read
        if len(command) != 2:
            print(
                "Incorrect number of args " + str(len(command)) + ", but need: rdbin {name}")
            continue

        binF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".bin":
                binF = item
        if binF == "":
            print("BinaryFile " + str(command[1]) + " does not exist")
            continue

        print(binF.get_context())
        print("okrdbin")

    elif command[0] == 'delbin':  # delete
        if len(command) != 2:
            print(
                "Incorrect number of args " + str(len(command)) + ", but need: delbin {name}")
            continue

        binF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".bin":
                binF = item
        if binF == "":
            print("BinaryFile " + str(command[1]) + " does not exist")
            continue

        binF.delete()

        print("okdelbin")



    # buff
    elif command[0] == 'mkbuf':  # make
        if len(command) != 3:
            print("Incorrect number of args " + str(len(command)) + ", but need: mkbuf {name} {size}")
            continue
        if not command[2].isdigit():
            print("Size must be number: mkbuf {name} {size}")
            continue
        bufferfile = BufferFile(command[2], home, log, command[1])

        print("okmkbuf")

    elif command[0] == 'appqu':  # add item
        if len(command) != 3:
            print("Incorrect number of args " + str(len(command)) + ", but need: appqu {name} {item}")
            continue

        bufF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".buf":
                bufF = item
        if bufF == "":
            print("Buffer " + str(command[1]) + " does not exist")
            continue

        bufF.append_queue(command[2])

        print("okappqubuf")

    elif command[0] == 'popqu':  # pop item
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: popqu {name}")
            continue

        bufF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".buf":
                bufF = item
        if bufF == "":
            print("Buffer " + str(command[1]) + " does not exist")
            continue

        bufF.first_out()

        print("okpopbuf")

    elif command[0] == 'mvbuf':  # move
        if len(command) != 3:
            print(
                "Incorrect number of args " + str(len(command)) + ", but need: mvbuf {name_of_moving} {name_of_moveIn}")
            continue

        bufF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".buf":
                bufF = item
        if bufF == "":
            print("Buffer " + str(command[1]) + " does not exist")
            continue

        dir = ""
        for item in home.list:
            if item.get_name() == command[2]:
                dir = item
        if dir == "":
            print("Directory " + str(command[2]) + " does not exist")
            continue

        bufF.move(dir)

        print("okmvbuf")

    elif command[0] == 'rdbuf':  # read
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: rdbuf {name}")
            continue

        bufF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".buf":
                bufF = item

        if bufF == "":
            print("BufferFile " + str(command[1]) + " does not exist")
            continue

        for i in range(0, len(bufF.get_context())):
            print(bufF.get_context()[i])

        print("okrdbuf")

    elif command[0] == 'delbuf':  # delete
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: delbuf {name}")
            continue

        bufF = ""
        for item in home.list:
            if item.get_name() == command[1] + ".buf":
                bufF = item

        if bufF == "":
            print("BufferFile " + str(command[1]) + " does not exist")
            continue

        bufF.delete()

        print("okdelbuf")


    # log
    elif command[0] == 'mklog':  # make
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: mklog {name}")
            continue

        print("Can be only 1 logger")

    elif command[0] == 'mvlog':  # move
        if len(command) != 2:
            print("Incorrect number of args " + str(len(command)) + ", but need: mvlog {name}")
            continue

        print("Cannot move logger")

    elif command[0] == 'rdlog':  # read
        if len(command) != 1:
            print("Incorrect number of args " + str(len(command)) + ", but need: rdlog")
            continue

        for i in range(0, len(log.get_context())):
            print(log.get_context()[i])

    elif command[0] == 'dellog':  # delete
        if len(command) != 1:
            print("Incorrect number of args " + str(len(command)) + ", but need: dellpg")
            continue

        print("Cannot delete logger")

    # ex
    else:
        print("Unknown command")
