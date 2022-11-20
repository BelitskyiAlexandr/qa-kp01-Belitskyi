from directory import Directory


class LogTextFile:
    #Constr
    def __init__(self):
        self.__name = "Logs.lg"
        self.context = "Begginning:"
        self.__directory = None
        self.append_context("\n" + self.get_name() + ": created")


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name +".lg"
        self.append_context("\n" + self.get_name() + ": was renamed")
    

    #Move
    def move(self, new_repo):
        new_repo.list.append(self)
        if not self.__directory == None:
            self.__directory.list.remove(self)
        self.__directory = new_repo
        self.append_context("\n" + self.get_name() + ": moved to " + new_repo.get_name())

    #Read
    def get_context(self):
        return self.context

    def get_direcrory_name(self):
        return self.__directory.get_name()

    #Append
    def append_context(self, message: str):
        self.context += message

    # Destruc
    def delete(self):
        if(self.__name == "None"):
            raise FileExistsError("Logger not exists")
        self.__directory.list.remove(self)
        self.append_context("\n" + self.get_name() + ": was removed")
        self.__name = "None"
        