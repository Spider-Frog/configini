# configini
Small package to easily parse an .ini file.

## Basic usage
### Read values
#### config.ini:
```ini
[test]
str=test
int=1
float=1.0005
dec=1.5
bool=no
list=["test"]
dict={"list": [1, 2, 3]}
datetime=2021-04-02T05:44:20
date=2021-04-02
time=05:44
```

#### config.py:
```python
import configini

configini.read('filename.ini')

class Config:
    str_value = configini.String('test', 'str')
    int_value = configini.Integer('test', 'int')
    float_value = configini.Float('test', 'float')
    dec_value = configini.Decimal('test', 'dec')
    bool_value = configini.Boolean('test', 'bool')
    list_value = configini.List('test', 'list')
    dict_value = configini.Dict('test', 'dict')
    datetime_value = configini.DateTime('test', 'test_datetime')
    date_value = configini.DateTime('test', 'test_date', format='%Y-%m-%d')
    time_value = configini.DateTime('test', 'test_time', format='%H:%M:%S')
```

Then you can use your config variables like this:
#### main.py:
```python
# Import the config file
from config import Config

# Do whatever you want with it.
some_variable = Config.str_value
```

**Note:** With the _Boolean_ method, 1, 'true', 'yes' will be cast to True,
**Note:** Only use double quote for strings inside list, the json.loads() method is used for parsing to list.

### Default values
Default values will be used when the value inside the configurations file is empty.
You can change the default value by passing the _default_ parameter.
```python
configini.String('chapter', 'key', default='Hello world')
```

### Custom values
If you have a custom value that you want automatically to be cast to the right data type,
You can use the parent 'Variable' method with parameter data_type to any method to cast your value.

An example with uuid:
```python
configini.Variable('chapter', 'key', data_type=UUID)
```

### Environment variables
Configini also supports .env variables.\
In the following example the chapter is called 'foo', and the key is 'bar'.
It will first try and fetch the environment variable called 'FOO_BAR' before the .ini variables.

#### .env:
```dotenv
FOO_BAR=alpha
```

#### config.ini:
```ini
[foo]
bar=beta
```

#### output:
```python
>>> configini.Variable('foo', 'bar')
'alpha'
```

If you want to use a different environment variable name then the chapter_key format you can use the environment_var parameter:

#### .env:
```dotenv
BONG=alpha
```

#### output:
```python
>>> configini.Variable('foo', 'bar', environment_var='BONG')
'alpha'
```

### Ignore errors
If you don't want to deal with invalid formatting in your .ini file.
Set the flag ```configini.ignore_errors``` to True:
```python
configini.ignore_errors = True
```

## Data types
### String
Casts any value to a string, If value is empty None is returned.
```python
configini.String('chapter', 'key', default=None, environment_var=None)
```

### Integer
Casts any value to an int, If value is empty None is returned.\
___Note___: Will raise ```ValueError```, if value is not a valid number, when ```configini.ignore_errors``` is set to False.
```python
configini.Integer('chapter', 'key', default=None, environment_var=None)
```

### Float
Casts any value to a float, If value is empty None is returned.\
___Note___: Will raise ```ValueError```, if value is not a valid number, when ```configini.ignore_errors``` is set to False.
```python
configini.Float('chapter', 'key', default=None, environment_var=None)
```

### Decimal
Casts any value to a decimal.Decimal, If value is empty None is returned.\
___Note___: Will raise ```ValueError```, if value is not a valid number, when ```configini.ignore_errors``` is set to False.
```python
configini.Decimal('chapter', 'key', default=None, environment_var=None)
```

### Boolean
Casts any value to a bool.\
Returns True if value is 1, 'true' or 'yes'.\
Returns False if value is 0, 'false' or 'no'.\
Else value will be None.
```python
configini.Boolean('chapter', 'key', default=None, environment_var=None)
```

### List
Casts any value to a list.\
___Note___: Will raise ```json.decoder.JSONDecodeError```, if value is not a valid number, when ```configini.ignore_errors``` is set to False.\
___Note___: Method uses ```json.loads``` method to convert string to list, so only use double quotes.
```python
configini.List('chapter', 'key', default=[], environment_var=None)
```

### Dict
Casts any value to a list.\
___Note___: Will raise ```json.decoder.JSONDecodeError```, if value is not a valid number, when ```configini.ignore_errors``` is set to False.\
___Note___: Method uses ```json.loads``` method to convert string to list, so only use double quotes.
```python
configini.List('chapter', 'key', default={}, environment_var=None)
```

### DateTime
Casts any value to a datetime.datetime, If value is empty None is returned.\
Use the format parameter to change how the datetime is converted.\
___Note___: Will raise ```ValueError```, if value is not a valid number, when ```configini.ignore_errors``` is set to False.
```python
configini.Decimal('chapter', 'key', format='%Y-%m-%dT%H:%M:%S', default=None, environment_var=None)
```