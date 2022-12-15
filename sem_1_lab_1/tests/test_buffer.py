from ..bufferFile import BufferFile
from ..directory import Directory
import pytest

def test_init():    
    with pytest.raises(TypeError):
        BufferFile()

def test_name():
    dir = Directory()
    buf = BufferFile(5, dir)
    assert buf.get_name() == "Buffer.buf"
    buf.set_name("New name")
    assert buf.get_name() == "New name.buf"

def test_bad_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    buf = BufferFile(5, dir1)
    with pytest.raises(TypeError):
        buf.move()
    

def test_good_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    buf = BufferFile(5, dir1)
    buf.move(dir2)
    assert buf.get_direcrory_name() == "dir2" 

def test_content():
    dir = Directory()
    buf = BufferFile(5, dir)
    assert buf.get_context() == []

def test_delete():
    dir = Directory()
    buf = BufferFile(5, dir)
    buf.delete()
    assert buf.list == []

def test_queue():
    dir = Directory()
    buf = BufferFile(1, dir)
    buf.append_queue("ss")
    with pytest.raises(OverflowError):
        buf.append_queue("qq")
        
def test_pop():
    dir = Directory()
    buf = BufferFile(1, dir)
    buf.append_queue("ss")
    assert buf.first_out() == "ss"
    assert buf.list == []

def test_redelete():
    dir = Directory()
    buf = BufferFile(3, dir)
    buf.delete()
    with pytest.raises(FileExistsError):
        buf.delete()