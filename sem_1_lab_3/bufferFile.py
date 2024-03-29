from directory import Directory
from logtextfile import LogTextFile


class BufferFile:
    # Constr
    def __init__(self, size, directory, log, name):
        if name == "":
            name = "Buffer"
        for item in directory.list:
            if item.get_name() == name + ".buf":
                name += "*"
        self.__name = name + ".buf"
        self.__size = size
        self.list = list()
        self.__directory = directory
        directory.list.append(self)
        self.log = log
        self.log.append_context("\n" + self.get_name() + ": created")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name + ".buf"
        self.log.append_context("\n" + self.get_name() + ": was renamed")

    # Move
    def move(self, new_repo):
        new_repo.list.append(self)
        self.__directory.list.remove(self)
        for item in new_repo.list:
            if item.get_name() == self.__name:
                name = self.__name[0: self.__name.find('.')] + "`" + ".buf"
                self.__name = name
                break
        self.__directory = new_repo
        self.log.append_context("\n" + self.get_name() + ": moved to " + new_repo.get_name())

    # Read
    def get_context(self):
        return self.list

    def get_direcrory_name(self):
        return self.__directory.get_name()

    # Append
    def append_queue(self, item):
        if len(self.list) == self.__size:
            raise OverflowError("max size reached")
        self.list.append(item)
        self.log.append_context("\n" + self.get_name() + ": append queue")

    def first_out(self):
        self.log.append_context("\n" + self.get_name() + ": poped")
        return self.list.pop(0)

    # Destruc
    def delete(self):
        if (self.__name == "None"):
            raise FileExistsError("Buffer not exist")
        self.__directory.list.remove(self)
        self.log.append_context("\n" + self.get_name() + ": was removed")
        self.__name = "None"

