#########################################################################################################################
# Copyright (C) 2008 - 2024 Execute Software, LLC.  All rights reserved.
########################################################################################################################
from core.logs import logs

class trace:
    stream = logs.get("debug@logs/debug.log", logs.DEBUG)
    allow: bool = False

    def __init__(self):
        pass

    @classmethod
    def message(cls, msg: str) -> None:
        if cls.allow:
            cls.stream.debug(msg)