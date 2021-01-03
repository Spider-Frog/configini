import configparser
import os
import json


__config = configparser.ConfigParser()


def read(file):
    __config.read(file)


def get(chapter, key, default=None, data_type=str, environment_var=None):
    """
    Function to retrieve the value from the configurations file.

    :param str chapter: Name of the chapter inside the configurations file.
    :param str key: variable name inside the chapter.
    :param default: Value to default to, when no value is given.
    :param data_type: Data type the value should be cast to.
    :param str environment_var: Overwrites the chapter_key value.
    :return: The value from the configurations value after being parsed.
    """

    try:
        value = os.environ.get(environment_var or f"{chapter.upper()}_{key.upper()}") or \
                   __config[chapter.lower()][key.lower()] or \
                   default

        # If value is None just immediately return the default.
        if value is None and data_type != bool:
            return default

        # Else if value contains a dot, and needs to be cast as an integer.
        # Cast it to float first, then integer to prevent an exception.
        elif data_type == int and '.' in value:
            return int(float(value))

        # Else if value is 0 or false and needs to be cast to a boolean.
        # then just immediately return False
        elif data_type == bool and value in ('0', 'false', None):
            return False

        # Else if value is list then use the json to cast the string into a list.
        elif data_type in (list, dict):
            return json.loads(value)

        # Cast value to right data type.
        return data_type(value)
    except KeyError:
        # Return the default value.
        return default
