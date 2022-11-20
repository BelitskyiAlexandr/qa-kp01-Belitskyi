from binaryFile import BinaryFile
from directory import Directory
from bufferFile import BufferFile
from logtextfile import LogTextFile

log = LogTextFile()
home_dir= Directory("home")
log.move(home_dir)

dir1 = Directory("dir1")
dir1.move_repository(home_dir)
dir2 = Directory("dir2")
dir2.move_repository(dir1)

bin1 = BinaryFile(dir1, log)
bin2 = BinaryFile(dir1, log)
bin3 = BinaryFile(dir2, log)


buf = BufferFile(3, dir1, log)

home_dir.print_list()
dir1.print_list()
dir2.print_list()

#Editing
bin3.set_name("RenamedBin")
print(bin3.get_context())

#Buff
buf.append_queue("Smth1")
buf.append_queue("Smth2")
buf.append_queue("Smth3")
print("~~~~" + buf.get_name() +"~~~~")
print(buf.get_context())

buf.first_out()
print("~~~~" + buf.get_name() +"~~~~")
print(buf.get_context())

#Dir move
dir3 = Directory("dir3")
dir3.move_repository(dir2)
dir2.print_list()
dir2.move_repository(dir3)
dir3.print_list()
dir2.print_list()

#Ending
print("~~~~" + log.get_name() +"~~~~\n" + log.get_context())