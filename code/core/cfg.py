#########################################################################################################################
# Copyright (C) 2008 - 2024 Execute Software, LLC.  All rights reserved.
########################################################################################################################

import yaml

def cfg_read(path: str) -> any:
    try:
        with open(path, 'r') as stream:
            return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)