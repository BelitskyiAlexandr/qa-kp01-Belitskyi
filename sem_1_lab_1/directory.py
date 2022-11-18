#from binaryFile import BinaryFile

class Directory:
    #Constr
    def __init__(self, name = "autodir"):
        self.__name = name
        self.list = list() 
        print("Directory created")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
   
    def add_item(self, item):
        self.list.append(item)
    #Move
    def move_repository(self, new_repo):
        if new_repo in self.list:
            self.list.remove(new_repo)
            new_repo.list.append(self)
            return
        new_repo.list.append(self)

    #Read
    def print_list(self):
        #self.sort_list()   TODO
        for item in self.list:
            print(item.get_name())

    

    # Destruc
    def __del__(self):
        self.__name = "None"
        self.list = list() 
        print("Directory was removed")




'''
binaryFile = BinaryFile()

smt = [2, "Tom", 22.2, binaryFile]
#for item in smt:
#   print(item)

dir = Directory("dir")
dir1 = Directory("dir1")

dir.add_item(dir1)
dir.print_list()

dir.move_repository(dir1)
print("~~~~")
dir.print_list()
print("~~~~")
dir1.print_list()
'''