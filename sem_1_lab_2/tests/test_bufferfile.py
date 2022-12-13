import pytest

from bufferFile import BufferFile
from directory import Directory
from logtextfile import LogTextFile

def test_init():
    with pytest.raises(TypeError):
        BufferFile()


def test_name():
    dir = Directory()
    log = LogTextFile()
    buf = BufferFile(5, dir, log)
    assert buf.get_name() == "Buffer.buf"
    buf.set_name("New name")
    assert buf.get_name() == "New name.buf"


def test_good_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    log = LogTextFile()
    buf = BufferFile(5, dir1, log)
    buf.move(dir2)
    assert buf.get_direcrory_name() == "dir2"


def test_content():
    dir = Directory()
    log = LogTextFile()
    buf = BufferFile(5, dir, log)
    assert buf.get_context() == []


def test_delete():
    dir = Directory()
    log = LogTextFile()
    buf = BufferFile(5, dir, log)
    buf.delete()
    assert dir.list == []


def test_queue():
    dir = Directory()
    log = LogTextFile()
    buf = BufferFile(1, dir, log)
    buf.append_queue("ss")
    with pytest.raises(OverflowError):
        buf.append_queue("qq")


def test_pop():
    dir = Directory()
    log = LogTextFile()
    buf = BufferFile(1, dir, log)
    buf.append_queue("ss")
    assert buf.first_out() == "ss"
    assert buf.list == []


def test_redelete():
    dir = Directory()
    log = LogTextFile()
    buf = BufferFile(3, dir, log)
    buf.delete()
    with pytest.raises(FileExistsError):
        buf.delete()