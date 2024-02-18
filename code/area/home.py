########################################################################################################################
# Copyright (C) 2008 - 2024 Execute Software, LLC.  All rights reserved.
########################################################################################################################

# https://realpython.com/fastapi-python-web-apis/

from util.routeutil import route_create

# Base.
from fastapi import FastAPI
fapi = FastAPI()

# Configuration.
g_area = "/home"

# Definitions.

@fapi.get("/home")
async def root():
    return {"message", "Hello World"}

@fapi.get("/home/test")
async def test():
    pass