########################################################################################################################
# Copyright (C) 2008 - 2024 Execute Software, LLC.  All rights reserved.
########################################################################################################################

# https://realpython.com/fastapi-python-web-apis/
from fastapi import FastAPI
fapi = FastAPI()

@fapi.get("/")
async def root():
    return {"message", "Hello World"}