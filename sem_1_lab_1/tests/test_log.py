from ..logtextfile import LogTextFile
from ..directory import Directory
import pytest

def test_init():    
    with pytest.raises(TypeError):
        LogTextFile()

def test_name():
    dir = Directory()
    log = LogTextFile(dir)
    assert log.get_name() == "Logs.lg"
    log.set_name("New name")
    assert log.get_name() == "New name.lg"

def test_bad_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    log = LogTextFile(dir1)
    with pytest.raises(TypeError):
        log.move()
    

def test_good_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    log = LogTextFile(dir1)
    log.move(dir2)
    assert log.get_direcrory_name() == "dir2" 

def test_content():
    dir = Directory()
    log = LogTextFile(dir)
    assert log.get_context() == "Begginning:"
    log.append_context(" + some")
    assert log.get_context() == "Begginning: + some"
    

def test_delete():
    dir = Directory()
    log = LogTextFile(dir)
    log.delete()
    assert dir.list == []

def test_redelete():
    log = LogTextFile()
    log.delete()
    with pytest.raises(FileExistsError):
        log.delete()