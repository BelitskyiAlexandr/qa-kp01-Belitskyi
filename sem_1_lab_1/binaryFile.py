from directory import Directory

class BinaryFile:
    #Constr
    def __init__(self, directory):
        self.__name = "BinaryFile.bin"
        self.context = "Something is here"
        self.__directory = directory
        directory.list.append(self)
        print("Binary File created")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name + ".bin"
    
    #Move
    def move(self, new_repo):   
        new_repo.list.append(self)
        self.__directory.list.remove(self)
        self.__directory = new_repo


    #Read
    def get_context(self):
        return self.context

    def get_direcrory_name(self):
        return self.__directory.get_name()


    # Destruc
    def delete(self):
        self.__directory.list.remove(self)
        print("Binary file was removed")

