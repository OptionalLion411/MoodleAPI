from moodle import (
    __version__,
    Auth,
    Core,
    Enrol,
    Mdl,
    Mod,
    Tool,
    Moodle,
)
from moodle.__main__ import main


def test_version():
    assert __version__ == "0.23.8"


def test_moodle(moodle: Moodle):
    assert issubclass(Moodle, Mdl)
    assert isinstance(moodle, Moodle)
    assert isinstance(moodle.auth, Auth)
    assert isinstance(moodle.core, Core)
    assert isinstance(moodle.enrol, Enrol)
    assert isinstance(moodle.mod, Mod)
    assert isinstance(moodle.tool, Tool)


def test_main():
    assert callable(main)
