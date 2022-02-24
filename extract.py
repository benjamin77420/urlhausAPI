import re
from typing import Optional


def json_extract(obj, key, regex: Optional = None):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key, regex: Optional = None):
        """Recursively search for values of key in JSON tree."""
        if regex is not None:
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k in key and re.match(regex, v):
                        arr.append(v)
                    elif isinstance(v, (dict, list)):
                        extract(v, arr, key, regex)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key, regex)
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if k in key:
                    arr.append(v)
                elif isinstance(v, (dict, list)):
                    extract(v, arr, key, regex)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key, regex)
        return arr

    values = extract(obj, arr, key, regex)

    if len(values) == 0:
        return None

    return values


