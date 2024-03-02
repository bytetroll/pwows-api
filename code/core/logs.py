#########################################################################################################################
# Copyright (C) 2008 - 2024 Execute Software, LLC.  All rights reserved.
########################################################################################################################
import os
import logging
import logging.handlers

from core.fault import fault

# https://www.loggly.com/ultimate-guide/python-logging-basics/
# https://www.logicmonitor.com/blog/python-logging-levels-explained

class logs:
    FORMAT_DEFAULT = logging.BASIC_FORMAT

    ALL = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    streams: {str, logging.log} = {}

    def __init__(self):
        pass

    @classmethod
    def get(cls, tag: str, lvl: int = ALL) -> logging.log:
        # If a log stream is not created/registered, this will do so first before
        # returning.  To create a new log, 'tag@path' must be passed.
        if tag in cls.streams:
            return cls.streams.get(tag)

        ptag: str = None
        ppath: str = None
        if '@' in tag:
            parts: [str] = tag.split("@")
            ptag = parts[0]
            ppath = parts[1]
            os.makedirs(os.path.dirname(ppath), exist_ok = True)
        if ppath is None:
            raise fault(f"Log stream for tag '{tag}' has not been created and no path has been specified.")

        # Right now we're only support file handlers.
        fmt: logging.Formatter = logging.Formatter(cls.FORMAT_DEFAULT)
        fh: logging.handlers.WatchedFileHandler = logging.FileHandler(ppath, mode = "w", encoding = "UTF-8", delay = False)
        fh.setFormatter(fmt)
        log: logging.Logger = logging.getLogger()
        if lvl != cls.ALL:
            log.setLevel(lvl)
        log.addHandler(fh)
        cls.streams[tag] = log
        return log