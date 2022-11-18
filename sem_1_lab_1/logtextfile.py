from directory import Directory


class LogTextFile:
    #Constr
    def __init__(self, directory):
        self.__name = "Logs.lg"
        self.context = "Begginning:"
        self.__directory = directory
        directory.list.append(self)
        print("Log File created")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name +".lg"

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

    #Append
    def append_context(self, message):
        self.context += message

    # Destruc
    def delete(self):
        self.__directory.list.remove(self)
        print("Log file was removed")
