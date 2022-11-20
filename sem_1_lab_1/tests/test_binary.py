from ..binaryFile import BinaryFile
from ..directory import Directory
import pytest

def test_init():    
    with pytest.raises(TypeError):
        BinaryFile()

def test_name():
    dir = Directory()
    bin = BinaryFile(dir)
    assert bin.get_name() == "BinaryFile.bin"
    bin.set_name("New name")
    assert bin.get_name() == "New name.bin"


def test_bad_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    bin = BinaryFile(dir1)
    with pytest.raises(TypeError):
        bin.move()
    

def test_good_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    bin = BinaryFile(dir1)
    bin.move(dir2)
    assert bin.get_direcrory_name() == "dir2" 

def test_content():
    dir = Directory()
    bin = BinaryFile(dir)
    assert bin.get_context() == "Something is here"

def test_delete():
    dir = Directory()
    bin = BinaryFile(dir)
    bin.delete()
    assert dir.list == []

def test_redelete():
    dir = Directory()
    bin = BinaryFile(dir)
    bin.delete()
    with pytest.raises(FileExistsError):
        bin.delete()