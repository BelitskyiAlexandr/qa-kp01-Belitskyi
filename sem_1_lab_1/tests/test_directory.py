from ..directory import Directory
import pytest

def test_init(): 
    dir = Directory()
    assert dir.get_name == "autodir"
    dir.set_name("dir1")
    assert dir.get_name == "dir1"   

def test_bad_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    with pytest.raises(TypeError):
        dir1.move()
    

def test_good_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    dir1.move_repository(dir2)
    assert dir1 in dir2.list 

def test_delete():
    dir = Directory()
    dir.delete()
    assert dir.list == []
    assert dir.get_name() == "None"

def test_redelete():
    dir = Directory()
    dir.delete()
    with pytest.raises(FileExistsError):
        dir.delete()
