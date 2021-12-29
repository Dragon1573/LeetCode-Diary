FIRST_BAD_VERSION = 0


def initialize(version: int) -> None:
    FIRST_BAD_VERSION = version


def isBadVersion(version: int) -> bool:
    return version >= FIRST_BAD_VERSION
