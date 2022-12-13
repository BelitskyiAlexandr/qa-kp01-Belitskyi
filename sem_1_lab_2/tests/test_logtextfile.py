import pytest

from directory import Directory
from logtextfile import LogTextFile



def test_name():
    log = LogTextFile()
    assert log.get_name() == "Logs.lg"
    log.set_name("New name")
    assert log.get_name() == "New name.lg"


def test_good_move():
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    log = LogTextFile()
    log.move(dir2)
    assert log.get_direcrory_name() == "dir2"


def test_content():
    log = LogTextFile()
    assert log.get_context() == "Begginning:\nLogs.lg: created"
    log.append_context(" + some")
    assert log.get_context() == "Begginning:\nLogs.lg: created + some"


def test_delete():
    dir = Directory()
    log = LogTextFile()
    log.move(dir)
    log.delete()
    assert dir.list == []


def test_redelete():
    dir = Directory()
    log = LogTextFile()
    log.move(dir)
    log.delete()
    with pytest.raises(FileExistsError):
        log.delete()