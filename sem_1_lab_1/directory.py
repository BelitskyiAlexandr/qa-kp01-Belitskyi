
class Directory:
    
    #Constr
    def __init__(self, name, logg):
        self.__name = ""
        if name == "":
            self.__name = "autodir"
        else: 
            self.__name = name
        self.list = list() 
        self.log = logg

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    #Move
    def move_repository(self, new_repo):
        if new_repo in self.list:
            self.list.remove(new_repo)
            new_repo.list.append(self)
            return
        new_repo.list.append(self)
        self.directory = new_repo

    #Read

    def sort_list(self):
        new_dir_list = []
        for item in self.list:
            if not item.get_name().endswith(".bin") or not item.get_name().endswith(".buf") or not item.get_name().endswith(".lg"):
                new_dir_list.append(item)
        for item in self.list:
            if item.get_name().endswith(".bin"):
                new_dir_list.append(item)
        for item in self.list:
            if item.get_name().endswith(".buf"):
                new_dir_list.append(item)
        for item in self.list:
            if item.get_name().endswith(".lg"):
                new_dir_list.append(item)
        self.list = new_dir_list
        


    def print_list(self):
        #self.sort_list()   
        print("~~~~" + self.get_name() + "~~~~")
        for item in self.list:
            if(item.get_name().endswith(".bin")):
                print("\033[31m{}\033[0m".format(item.get_name()))
                continue
            elif(item.get_name().endswith(".buf")):
                print("\033[32m{}\033[0m".format(item.get_name()))
                continue
            elif(item.get_name().endswith(".lg")):
                print("\033[33m{}\033[0m".format(item.get_name()))
                continue
            else:
                print("\033[34m{}\033[0m".format(item.get_name()))

    

    # Destruc
    def delete(self):
        self.__name = "None"
        self.list = list()
        print(self.get_name() + " was removed")
