from directory import Directory

class BufferFile:
    #Constr
    def __init__(self, size, directory):
        self.__name = "Buffer.buf"
        self.__size = size
        self.list = list()
        self.__directory = directory
        directory.list.append(self)
        print("Buffer File created")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name + ".buf"
    
    
    #Move
    def move(self, new_repo):   
        new_repo.list.append(self)
        self.__directory.list.remove(self)
        self.__directory = new_repo


    #Read       TODO
    def get_context(self):
        return self.list

    def get_direcrory_name(self):
        return self.__directory.get_name()


    #Append
    def append_queue(self, item):
        if len(self.list) == self.__size:
            raise OverflowError("max size reached")
        self.list.append(item)

    def first_out(self):
        return self.list.pop(0)

    # Destruc
    def delete(self):
        self.__directory.list.remove(self)
        print("Buf file was removed")


