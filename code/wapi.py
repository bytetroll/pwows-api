########################################################################################################################
# Copyright (C) 2008 - 2024 Execute Software, LLC.  All rights reserved.
########################################################################################################################

# https://realpython.com/fastapi-python-web-apis/
# https://stackoverflow.com/questions/73908734/how-to-run-uvicorn-fastapi-server-as-a-module-from-another-python-file

from core.trace import trace
from core.cfg import cfg_read
from core.fault import fault

import uvicorn
from uvicorn.main import main
import webbrowser
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

wapi: FastAPI = FastAPI(title = "PWOWS - (RESTful)WebAPI")

if __name__ == "__main__":
    cfg: {} = cfg_read("cfg/wapi.yaml")
    dbg: bool = bool(cfg["runtime"]["debug"])
    trace.allow = dbg

    trace.message("Parsed core configuration (wapi.yaml).")
    rev: int = int(cfg["revision"])
    ver: str = f"Revision: {rev} ({"Debug" if dbg else "Release"})"
    trace.message(f"Build: {ver}")

    adr: str = cfg["host"]["address"]
    port: int = int(cfg["host"]["port"])
    rload: bool = cfg["host"]["reload"]
    thrds: int = int(cfg["host"]["threads"])

    trace.message(f"Starting wapi on '{adr}:{port}' with reload = {rload}.  Allocated threads = {thrds}.")
    uvicorn.run("wapi:wapi", host = adr, port = port, reload = rload, workers = thrds)

# @wapi.get("/")
# async def root() -> None:
#     return {"message": "Hello World"}