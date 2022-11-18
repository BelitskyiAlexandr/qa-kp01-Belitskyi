from directory import Directory

class BinaryFile:
    #Constr
    def __init__(self, directory):
        self.__name = "BinaryFile"
        self.context = "Something is here"
        self.__directory = directory
        directory.list.append(self)
        print("Binary File created")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    #Move
    def move(self, new_repo):   
        new_repo.list.append(self)
        self.__directory.list.remove(self)
        self.__directory = new_repo


    #Read
    def get_context(self):
        print(self.context)

    def get_direcrory_name(self):
        print(self.__directory.get_name())


    # Destruc
    def __del__(self):
        print("Binary file was removed")

dir1 = Directory("dir1")
dir2 = Directory()

bin = BinaryFile(dir1)

bin.get_direcrory_name()
bin.move(dir2)
bin.get_direcrory_name()
