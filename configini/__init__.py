import configparser
from typing import Union
import os
import json
import decimal
import datetime

__config = configparser.ConfigParser()

ignore_errors = False


def read(file):
    __config.read(file)


def Variable(chapter: str, key: str, data_type: Union[str, int, float, decimal.Decimal, bool, list, dict, object],
             default=None, environment_var=None):
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

        if value is not None:
            return data_type(value)

        return value
    except KeyError:
        # Return the default value.
        return default


def String(chapter: str, key: str, default=None, environment_var=None):
    """
    Function to retrieve a string value from the configurations file.

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: str
    """
    return Variable(chapter, key, default=default, data_type=str, environment_var=environment_var)


def Integer(chapter: str, key: str, default=None, environment_var=None):
    """
    Function to retrieve a integer value from the configurations file.

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: int
    """

    try:
        return Variable(chapter, key, default=default, data_type=int, environment_var=environment_var)
    except ValueError as E:
        if ignore_errors:
            return default
        else:
            raise E


def Float(chapter: str, key: str, default=None, environment_var=None):
    """
    Function to retrieve a float value from the configurations file.

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: float
    """

    try:
        return Variable(chapter, key, default=default, data_type=float, environment_var=environment_var)
    except ValueError as E:
        if ignore_errors:
            return default
        else:
            raise E


def Decimal(chapter: str, key: str, default=None, environment_var=None):
    """
    Function to retrieve a decimal.Decimal value from the configurations file.

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: decimal
    """

    try:
        return Variable(chapter, key, default=default, data_type=decimal.Decimal, environment_var=environment_var)
    except decimal.InvalidOperation as E:
        if ignore_errors:
            return default
        else:
            raise E


def Boolean(chapter: str, key: str, default=None, environment_var=None):
    """
    Function to retrieve a boolean value from the configurations file.

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: boolean
    """
    value = Variable(chapter, key, default=default, data_type=str, environment_var=environment_var)

    if type(value) is str:
        if value.upper() in ('1', 'TRUE', 'YES'):
            return True
        elif value.upper() in ('0', 'FALSE', 'NO'):
            return False
        else:
            return default

    return None


def List(chapter: str, key: str, default=None, environment_var=None):
    """
    Function to retrieve a list value from the configurations file.

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: list
    """

    if default is None:
        default = []

    value = Variable(chapter, key, default=default, data_type=str, environment_var=environment_var)

    try:
        return json.loads(value)
    except json.decoder.JSONDecodeError as E:
        if ignore_errors:
            return default
        else:
            raise E


def Dict(chapter: str, key: str, default=None, environment_var=None):
    """
    Function to retrieve a dict value from the configurations file.

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: dict
    """

    if default is None:
        default = {}

    value = Variable(chapter, key, default=default, data_type=str, environment_var=environment_var)

    try:
        return json.loads(value)
    except json.decoder.JSONDecodeError as E:
        if ignore_errors:
            return default
        else:
            raise E


def DateTime(chapter: str, key: str, format='%Y-%m-%dT%H:%M:%S', default=None, environment_var=None):
    """
    Function to retrieve a datetime.datetime value from the configurations file.
    Datetime format: %Y-%m-%sT%H:%M:%S

    :param chapter: Name of the chapter inside the configurations file.
    :type chapter: str
    :param key: Variable name inside the chapter.
    :type key: str
    :param format: Format used to parse string to datetime object.
    :type format: str
    :param default: Value to default to, when no value is given.
    :param environment_var: Used to search for environment variables instead of using chapter_key name.
    :type environment_var: str
    :return: The value from the configurations file after being parsed.
    :rtype: datetime.datetime
    """

    value = Variable(chapter, key, default=default, data_type=str, environment_var=environment_var)

    try:
        return datetime.datetime.strptime(value, format)
    except ValueError as E:
        if ignore_errors:
            return default
        else:
            raise E
