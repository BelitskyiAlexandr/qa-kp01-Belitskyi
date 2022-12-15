import pytest

from binary_file import BinaryFile
from directory import Directory
from logtextfile import LogTextFile

def test_init():
    with pytest.raises(TypeError):
        BinaryFile()

def test_name():
    dir = Directory()
    log = LogTextFile()
    bin = BinaryFile(dir, log, "")
    assert bin.get_name() == "BinaryFile.bin"
    bin.set_name("New name")
    assert bin.get_name() == "New name.bin"


def test_good_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    log = LogTextFile()
    bin = BinaryFile(dir1, log, "")
    bin.move(dir2)
    assert bin.get_direcrory_name() == "dir2"


def test_name_after_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    log = LogTextFile()
    bin1 = BinaryFile(dir1, log, "")
    bin2 = BinaryFile(dir2, log, "")
    bin1.move(dir2)
    assert bin1.get_name() == "BinaryFile`.bin"


def test_content():
    dir = Directory()
    log = LogTextFile()
    bin = BinaryFile(dir, log, "")
    assert bin.get_context() == "Something is here"


def test_delete():
    dir = Directory()
    log = LogTextFile()
    bin = BinaryFile(dir, log, "")
    bin.delete()
    assert dir.list == []


def test_redelete():
    dir = Directory()
    log = LogTextFile()
    bin = BinaryFile(dir, log, "")
    bin.delete()
    with pytest.raises(FileExistsError):
        bin.delete()