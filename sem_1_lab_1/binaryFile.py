from directory import Directory
from logtextfile import LogTextFile

class BinaryFile:
    #Constr
    def __init__(self, directory, logg):
        self.__name = "BinaryFile.bin"
        self.context = "Something is here"
        self.__directory = directory
        directory.list.append(self)
        self.log = logg
        self.log.append_context("\n" + self.get_name() + ": created")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name + ".bin"
        self.log.append_context("\n" + self.get_name() + ": was renamed")
    
    #Move
    def move(self, new_repo):   
        new_repo.list.append(self)
        self.__directory.list.remove(self)
        self.__directory = new_repo
        self.log.append_context("\n" + self.get_name() + ": moved to " + new_repo.get_name())


    #Read
    def get_context(self):
        return self.context

    def get_direcrory_name(self):
        return self.__directory.get_name()


    # Destruc
    def delete(self):
        if(self.__name == "None"):
            raise FileExistsError("Binary file not exists")
        self.__directory.list.remove(self)
        self.append_context("\n" + self.get_name() + ": was removed")
        self.__name = "None"

