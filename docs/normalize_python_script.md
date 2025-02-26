# Normalize python code
When you publish a python code, you should normalize your code, so everyone can read it and understand it easily.
In this doc, we will learn:
- how the python code naming convention works
- how to keep your code clean and respect coding standard
    - how to use tools such as `black`, "pylint" to keep your code clean(code lint). 
    - how to use tools such as `isort` to clean imports
    - how to use `type hint` and use tool such as `` to do static check
- how to document the code
- how to test the code
- how to versioning the code

## 1. Naming convention

The python naming convention is defined in **PEP08**. For more details, you should visit the official page of PEP.

### 1.1 Package

A **package name** should always be in `lowercase letters`, and separate words with `underscores` only if necessary.

```text
my_package   # Good ✅
mypackage    # Good (preferred if short) ✅
MyPackage    # Bad (avoid CamelCase for packages) ❌ 
myPackage    # Bad (mixed case is not recommended) ❌ 
```

### 1.2 Module

A **module name** should always be in `lowercase letters`, and separate words with `underscores` only if it improves readability.

```text
my_module.py   # Good ✅
mymodule.py    # Good (preferred if short) ✅
MyModule.py    # Bad (avoid CamelCase for packages) ❌ 
myModule.py    # Bad (mixed case is not recommended) ❌ 
my-module.py   # Not allowed (hyphens are not allowed) ❌❌
```

### 1.3 Class

A class name should be in CamelCase (PascalCase).

```text
class MyClass:   # Good ✅
    pass

class my_class:  # Bad (use CamelCase) ❌ 
    pass

class my_class:   # Bad (not readable) ❌ 
    pass
```

### 1.4 Function/Method

A **function/method** name should use the `snake_case (lowercase with underscores)`.

```text
def my_function():  # Good ✅
    pass

def MyFunction():   # Bad (looks like a class) ❌ 
    pass

def myFunction():   # Bad (mixed case is not recommended) ❌ 
    pass
```

### 1.5 Variable

Use `snake_case` for variable names.

```text
my_variable = 38   # Good ✅
MyVariable = 38    # Bad (avoid CamelCase for variables) ❌ 
myVariable = 38    # Bad (mixed case is not recommended) ❌ 
```

### 1.6 Constant

```text
MY_CONSTANT = 38  # Good ✅
pi = 3.14        # Bad (constants should be in ALL_CAPS) ❌ 
```

### 1.7 Custom exception 

The custom exception name should be in `CamelCase` and end with `Error`.

```text
class DataProcessingError(Exception):  # Good ✅
    pass

class Data_Error(Exception):  # Bad (no underscores in class names) ❌ 
    pass
```

## 2. Private and Protected Members of Python class 

In a python class, you can define:
- `private` attributes/methods with a single underscore _ .
- `strong private` attributes/methods with a double underscore __ (name mangling) .

```python
class MyClass:
    def __init__(self):
        self.public_var = 42         # Public attribute
        self._protected_var = 99      # Protected attribute (convention)
        self.__private_var = 100      # Private attribute (name mangling)

    def _helper_method(self):         # Protected method
        pass

    def __internal_method(self):      # Private method
        pass

```

> Another class can still access the protected attribute of a class, it's only a naming convention that tells other users
> you should not use it.
> 
> 

## 3. Keep your code clean and readable

We have seen the naming convention for python packages, classes, etc. Python also has other convention on how to write
the code(e.g. line length,). We can use tools such as `pylint` and `black` to help you keep your code inline with these
conventions. 


### 3.1 pylint 

**pylint** is a tool that checks for `anomalies(violating a coding standard)` in source code, giving us immediate 
feedbacks. After analyzing the code it gives an overall score out of 10 along with `anomalies details` in the source 
code.

```shell
pip install pylint

# analyse code quality of all files in a directory
pylint ./src/stock_catcher

```

You can customize the coding standard which pylint uses in `.pylintrc` . If you provide nothing, a default one will be used.
You can find an example of `.pylintrc` in appendix


### 3.2 Use black to format your source code

pylint can detect the `anomalies`, but you need to correct them by yourself. **black** is a great tool for 
formatting your Python code automatically.

```shell
pip install black

black ./src/stock_catcher
```

### 3.3. Use isort to format your import

**isort** automatically sorts and organizes imports.

```shell
pip install isort

# use the default config, if you have config in your pyproject.toml, the provided config will be used
isort ./src/stock_catcher

# you can also use the black profile
isort --profile=black
```
### 3.4 Type checking with mypy

Mypy is a static type checker for Python. But it only checks the function with type hints, if you have nothing in function
definition, it will do nothing.

```shell
pip install mypy
mypy ./src/stock_catcher
```

## 4. Document the source code
We have three types of code documentation in python:
- comments on codes
- type hints
- docstring

### 4.1 Comments on codes
When your code is complicated, you should add comments to clarify the code. In python an inline comment starts
with `#`. There is no clear rules on how to write comments, the goal is to help you or others to understand why you
write code like this. 

Below is a good example,

```shell
# Using dictionary comprehension for efficiency
squared_numbers = {x: x**2 for x in range(10)}

```

### 4.2 type hints

Python supports type hints for function arguments and return values. Use them to improve code clarity.

### 4.3 Docstrings

Python follows [PEP 257](https://peps.python.org/pep-0257/) for docstrings.

You can use docstrings to document `modules, classes, functions, and methods`.

Docstrings has many different styles, such as :
- Google Style, 
- NumPy Style, 
- reStructuredText

Here, I use `reStructuredText`, because it's supported by `Sphinx` and `pypi`.

#### 4.3.1 Module docstring

In python, a `file.py is considered as a module` which can contain `one or more class`. It should contain a docstring,
that describes its purpose. To do so, at the beginning of the Python file, add the below text

```python
"""
catcher
===========

This module provides functions to get the latest news of French stock.

Author:
    Pengfei liu

Date:
    2025-02-25
"""

```
#### 4.4.2 class docstring

The class should have a class level docstring which contains the description of the class, the params for the constructor
and the internal variables.

In the below example, we have a class called `StockAnalyzer`, the constructor requires one parameter called `stock_ticker`
, it contains one internal variable called `stock_ticker`.

```python
class StockAnalyzer:
    """
    Represents a stock analyzer in the system.

    :param stock_ticker: The stock's unique identifier
    :type stock_ticker: str
       

    :ivar stock_ticker: The stock's unique identifier
    :vartype stock_ticker: str

    """

    ALLOW_TICKERS = ["ticker1", "ticker2"]
    
    def __init__(self, stock_ticker:str):
        """
        Initializes a stock analyzer instance.
        :param stock_ticker: The stock's unique identifier
        :type stock_ticker: str
        """
        self.stock_ticker = stock_ticker
        
```

#### 4.3.3 Function/method docstring 

The below example shows docstring of a method, it has input and output parameters. It also raises exception.

```python
    def get_stock_latest_price(self,start_date:str,end_date:str)->pd.DataFrame:
        """
        This function takes a stock ticker and returns a Pandas DataFrame which contains the latest price of the stock
        within the given date range.
        :param start_date: start date
        :type start_date: str
        :param end_date: end date
        :type end_date: str
        :return: a pandas dataframe containing the latest price of the stock
        :rtype: pd.DataFrame
        :raise ValueError: if stock ticker does not exist

        :Example:

        .. code-block:: python
           stock_analyzer = StockAnalyzer("ticker1")
           stock_analyzer.get_stock_latest_price(start_date="2020-01-01",end_date="2020-02-25")
        """
        result = pd.DataFrame()
        if self.stock_ticker not in StockAnalyzer.ALLOW_TICKERS:
            raise ValueError(f"The stock ticker {self.stock_ticker} is no longer valid.")
        print(f"Getting latest price for stock ticker: {self.stock_ticker} with start date: {start_date} and end date: {end_date}")
        return result
```

> You can find the complete example in `src/stock_catcher/analyzer.py`
> 
### 4.4 Generate a html documentation with Sphinx

## Appendix 

## pylint config

```ini
[MAIN]

# Specify a configuration file.
#rcfile=

# Python code to execute, usually for sys.path manipulation such as
# pygtk.require().
#init-hook=

# Files or directories to be skipped. They should be base names, not
# paths.
ignore=CVS

# Add files or directories matching the regex patterns to the ignore-list. The
# regex matches against paths and can be in Posix or Windows format.
ignore-paths=

# Files or directories matching the regex patterns are skipped. The regex
# matches against base names, not paths.
ignore-patterns=^\.#

# Pickle collected data for later comparisons.
persistent=yes

# List of plugins (as comma separated values of python modules names) to load,
# usually to register additional checkers.
load-plugins=
    pylint.extensions.check_elif,
    pylint.extensions.bad_builtin,
    pylint.extensions.docparams,
    pylint.extensions.for_any_all,
    pylint.extensions.set_membership,
    pylint.extensions.code_style,
    pylint.extensions.overlapping_exceptions,
    pylint.extensions.typing,
    pylint.extensions.redefined_variable_type,
    pylint.extensions.comparison_placement,

# Use multiple processes to speed up Pylint. Specifying 0 will auto-detect the
# number of processors available to use.
jobs=1

# When enabled, pylint would attempt to guess common misconfiguration and emit
# user-friendly hints instead of false-positive error messages.
suggestion-mode=yes

# Allow loading of arbitrary C extensions. Extensions are imported into the
# active Python interpreter and may run arbitrary code.
unsafe-load-any-extension=no

# A comma-separated list of package or module names from where C extensions may
# be loaded. Extensions are loading into the active Python interpreter and may
# run arbitrary code
extension-pkg-allow-list=

# Minimum supported python version
py-version = 3.7.2

# Control the amount of potential inferred values when inferring a single
# object. This can help the performance when dealing with large functions or
# complex, nested conditions.
limit-inference-results=100

# Specify a score threshold to be exceeded before program exits with error.
fail-under=10.0

# Return non-zero exit code if any of these messages/categories are detected,
# even if score is above --fail-under value. Syntax same as enable. Messages
# specified are enabled, while categories only check already-enabled messages.
fail-on=


[MESSAGES CONTROL]

# Only show warnings with the listed confidence levels. Leave empty to show
# all. Valid levels: HIGH, INFERENCE, INFERENCE_FAILURE, UNDEFINED
# confidence=

# Enable the message, report, category or checker with the given id(s). You can
# either give multiple identifier separated by comma (,) or put this option
# multiple time (only on the command line, not in the configuration file where
# it should appear only once). See also the "--disable" option for examples.
enable=
    use-symbolic-message-instead,
    useless-suppression,

# Disable the message, report, category or checker with the given id(s). You
# can either give multiple identifiers separated by comma (,) or put this
# option multiple times (only on the command line, not in the configuration
# file where it should appear only once).You can also use "--disable=all" to
# disable everything first and then re-enable specific checks. For example, if
# you want to run only the similarities checker, you can use "--disable=all
# --enable=similarities". If you want to run only the classes checker, but have
# no Warning level messages displayed, use"--disable=all --enable=classes
# --disable=W"

disable=
    attribute-defined-outside-init,
    invalid-name,
    missing-docstring,
    protected-access,
    too-few-public-methods,
    # handled by black
    format,
    # We anticipate #3512 where it will become optional
    fixme,
    cyclic-import,


[REPORTS]

# Set the output format. Available formats are text, parseable, colorized, msvs
# (visual studio) and html. You can also give a reporter class, eg
# mypackage.mymodule.MyReporterClass.
output-format=text

# Tells whether to display a full report or only the messages
reports=no

# Python expression which should return a note less than 10 (10 is the highest
# note). You have access to the variables 'fatal', 'error', 'warning', 'refactor', 'convention'
# and 'info', which contain the number of messages in each category, as
# well as 'statement', which is the total number of statements analyzed. This
# score is used by the global evaluation report (RP0004).
evaluation=max(0, 0 if fatal else 10.0 - ((float(5 * error + warning + refactor + convention) / statement) * 10))

# Template used to display messages. This is a python new-style format string
# used to format the message information. See doc for all details
#msg-template=

# Activate the evaluation score.
score=yes


[LOGGING]

# Logging modules to check that the string format arguments are in logging
# function parameter format
logging-modules=logging

# The type of string formatting that logging methods do. `old` means using %
# formatting, `new` is for `{}` formatting.
logging-format-style=old


[MISCELLANEOUS]

# List of note tags to take in consideration, separated by a comma.
notes=FIXME,XXX,TODO

# Regular expression of note tags to take in consideration.
#notes-rgx=


[SIMILARITIES]

# Minimum lines number of a similarity.
min-similarity-lines=6

# Ignore comments when computing similarities.
ignore-comments=yes

# Ignore docstrings when computing similarities.
ignore-docstrings=yes

# Ignore imports when computing similarities.
ignore-imports=yes

# Signatures are removed from the similarity computation
ignore-signatures=yes


[VARIABLES]

# Tells whether we should check for unused import in __init__ files.
init-import=no

# A regular expression matching the name of dummy variables (i.e. expectedly
# not used).
dummy-variables-rgx=_$|dummy

# List of additional names supposed to be defined in builtins. Remember that
# you should avoid defining new builtins when possible.
additional-builtins=

# List of strings which can identify a callback function by name. A callback
# name must start or end with one of those strings.
callbacks=cb_,_cb

# Tells whether unused global variables should be treated as a violation.
allow-global-unused-variables=yes

# List of names allowed to shadow builtins
allowed-redefined-builtins=

# Argument names that match this expression will be ignored. Default to name
# with leading underscore.
ignored-argument-names=_.*

# List of qualified module names which can have objects that can redefine
# builtins.
redefining-builtins-modules=six.moves,past.builtins,future.builtins,builtins,io


[FORMAT]

# Maximum number of characters on a single line.
max-line-length=100

# Regexp for a line that is allowed to be longer than the limit.
ignore-long-lines=^\s*(# )?<?https?://\S+>?$

# Allow the body of an if to be on the same line as the test if there is no
# else.
single-line-if-stmt=no

# Allow the body of a class to be on the same line as the declaration if body
# contains single statement.
single-line-class-stmt=no

# Maximum number of lines in a module
max-module-lines=2000

# String used as indentation unit. This is usually "    " (4 spaces) or "\t" (1
# tab).
indent-string='    '

# Number of spaces of indent required inside a hanging or continued line.
indent-after-paren=4

# Expected format of line ending, e.g. empty (any line ending), LF or CRLF.
expected-line-ending-format=


[BASIC]

# Good variable names which should always be accepted, separated by a comma
good-names=i,j,k,ex,Run,_

# Good variable names regexes, separated by a comma. If names match any regex,
# they will always be accepted
good-names-rgxs=

# Bad variable names which should always be refused, separated by a comma
bad-names=foo,bar,baz,toto,tutu,tata

# Bad variable names regexes, separated by a comma. If names match any regex,
# they will always be refused
bad-names-rgxs=

# Colon-delimited sets of names that determine each other's naming style when
# the name regexes allow several styles.
name-group=

# Include a hint for the correct naming format with invalid-name
include-naming-hint=no

# Naming style matching correct function names.
function-naming-style=snake_case

# Regular expression matching correct function names
function-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming style matching correct variable names.
variable-naming-style=snake_case

# Regular expression matching correct variable names
variable-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming style matching correct constant names.
const-naming-style=UPPER_CASE

# Regular expression matching correct constant names
const-rgx=(([A-Z_][A-Z0-9_]*)|(__.*__))$

# Naming style matching correct attribute names.
attr-naming-style=snake_case

# Regular expression matching correct attribute names
attr-rgx=[a-z_][a-z0-9_]{2,}$

# Naming style matching correct argument names.
argument-naming-style=snake_case

# Regular expression matching correct argument names
argument-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming style matching correct class attribute names.
class-attribute-naming-style=any

# Regular expression matching correct class attribute names
class-attribute-rgx=([A-Za-z_][A-Za-z0-9_]{2,30}|(__.*__))$

# Naming style matching correct class constant names.
class-const-naming-style=UPPER_CASE

# Regular expression matching correct class constant names. Overrides class-
# const-naming-style.
#class-const-rgx=

# Naming style matching correct inline iteration names.
inlinevar-naming-style=any

# Regular expression matching correct inline iteration names
inlinevar-rgx=[A-Za-z_][A-Za-z0-9_]*$

# Naming style matching correct class names.
class-naming-style=PascalCase

# Regular expression matching correct class names
class-rgx=[A-Z_][a-zA-Z0-9]+$


# Naming style matching correct module names.
module-naming-style=snake_case

# Regular expression matching correct module names
module-rgx=(([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$


# Naming style matching correct method names.
method-naming-style=snake_case

# Regular expression matching correct method names
method-rgx=[a-z_][a-z0-9_]{2,}$

# Regular expression which can overwrite the naming style set by typevar-naming-style.
#typevar-rgx=

# Regular expression which should only match function or class names that do
# not require a docstring. Use ^(?!__init__$)_ to also check __init__.
no-docstring-rgx=__.*__

# Minimum line length for functions/classes that require docstrings, shorter
# ones are exempt.
docstring-min-length=-1

# List of decorators that define properties, such as abc.abstractproperty.
property-classes=abc.abstractproperty


[TYPECHECK]

# Regex pattern to define which classes are considered mixins if ignore-mixin-
# members is set to 'yes'
mixin-class-rgx=.*MixIn

# List of module names for which member attributes should not be checked
# (useful for modules/projects where namespaces are manipulated during runtime
# and thus existing member attributes cannot be deduced by static analysis). It
# supports qualified module names, as well as Unix pattern matching.
ignored-modules=

# List of class names for which member attributes should not be checked (useful
# for classes with dynamically set attributes). This supports the use of
# qualified names.
ignored-classes=SQLObject, optparse.Values, thread._local, _thread._local

# List of members which are set dynamically and missed by pylint inference
# system, and so shouldn't trigger E1101 when accessed. Python regular
# expressions are accepted.
generated-members=REQUEST,acl_users,aq_parent,argparse.Namespace

# List of decorators that create context managers from functions, such as
# contextlib.contextmanager.
contextmanager-decorators=contextlib.contextmanager

# Tells whether to warn about missing members when the owner of the attribute
# is inferred to be None.
ignore-none=yes

# This flag controls whether pylint should warn about no-member and similar
# checks whenever an opaque object is returned when inferring. The inference
# can return multiple potential results while evaluating a Python object, but
# some branches might not be evaluated, which results in partial inference. In
# that case, it might be useful to still emit no-member and other checks for
# the rest of the inferred objects.
ignore-on-opaque-inference=yes

# Show a hint with possible names when a member name was not found. The aspect
# of finding the hint is based on edit distance.
missing-member-hint=yes

# The minimum edit distance a name should have in order to be considered a
# similar match for a missing member name.
missing-member-hint-distance=1

# The total number of similar names that should be taken in consideration when
# showing a hint for a missing member.
missing-member-max-choices=1

[SPELLING]

# Spelling dictionary name. Available dictionaries: none. To make it working
# install python-enchant package.
spelling-dict=

# List of comma separated words that should not be checked.
spelling-ignore-words=

# List of comma separated words that should be considered directives if they
# appear and the beginning of a comment and should not be checked.
spelling-ignore-comment-directives=fmt: on,fmt: off,noqa:,noqa,nosec,isort:skip,mypy:,pragma:,# noinspection

# A path to a file that contains private dictionary; one word per line.
spelling-private-dict-file=.pyenchant_pylint_custom_dict.txt

# Tells whether to store unknown words to indicated private dictionary in
# --spelling-private-dict-file option instead of raising a message.
spelling-store-unknown-words=no

# Limits count of emitted suggestions for spelling mistakes.
max-spelling-suggestions=2


[DESIGN]

# Maximum number of arguments for function / method
max-args=10

# Maximum number of locals for function / method body
max-locals=25

# Maximum number of return / yield for function / method body
max-returns=11

# Maximum number of branch for function / method body
max-branches=27

# Maximum number of statements in function / method body
max-statements=100

# Maximum number of parents for a class (see R0901).
max-parents=7

# List of qualified class names to ignore when counting class parents (see R0901).
ignored-parents=

# Maximum number of attributes for a class (see R0902).
max-attributes=11

# Minimum number of public methods for a class (see R0903).
min-public-methods=2

# Maximum number of public methods for a class (see R0904).
max-public-methods=25

# Maximum number of boolean expressions in an if statement (see R0916).
max-bool-expr=5

# List of regular expressions of class ancestor names to
# ignore when counting public methods (see R0903).
exclude-too-few-public-methods=

[CLASSES]

# List of method names used to declare (i.e. assign) instance attributes.
defining-attr-methods=__init__,__new__,setUp,__post_init__

# List of valid names for the first argument in a class method.
valid-classmethod-first-arg=cls

# List of valid names for the first argument in a metaclass class method.
valid-metaclass-classmethod-first-arg=mcs

# List of member names, which should be excluded from the protected access
# warning.
exclude-protected=_asdict,_fields,_replace,_source,_make

# Warn about protected attribute access inside special methods
check-protected-access-in-special-methods=no

[IMPORTS]

# List of modules that can be imported at any level, not just the top level
# one.
allow-any-import-level=

# Allow wildcard imports from modules that define __all__.
allow-wildcard-with-all=no

# Analyse import fallback blocks. This can be used to support both Python 2 and
# 3 compatible code, which means that the block might have code that exists
# only in one or another interpreter, leading to false positives when analysed.
analyse-fallback-blocks=no

# Deprecated modules which should not be used, separated by a comma
deprecated-modules=regsub,TERMIOS,Bastion,rexec

# Create a graph of every (i.e. internal and external) dependencies in the
# given file (report RP0402 must not be disabled)
import-graph=

# Create a graph of external dependencies in the given file (report RP0402 must
# not be disabled)
ext-import-graph=

# Create a graph of internal dependencies in the given file (report RP0402 must
# not be disabled)
int-import-graph=

# Force import order to recognize a module as part of the standard
# compatibility libraries.
known-standard-library=

# Force import order to recognize a module as part of a third party library.
known-third-party=enchant

# Couples of modules and preferred modules, separated by a comma.
preferred-modules=


[EXCEPTIONS]

# Exceptions that will emit a warning when being caught. Defaults to
# "Exception"
overgeneral-exceptions=Exception


[TYPING]

# Set to ``no`` if the app / library does **NOT** need to support runtime
# introspection of type annotations. If you use type annotations
# **exclusively** for type checking of an application, you're probably fine.
# For libraries, evaluate if some users what to access the type hints at
# runtime first, e.g., through ``typing.get_type_hints``. Applies to Python
# versions 3.7 - 3.9
runtime-typing = no


[DEPRECATED_BUILTINS]

# List of builtins function names that should not be used, separated by a comma
bad-functions=map,input


[REFACTORING]

# Maximum number of nested blocks for function / method body
max-nested-blocks=5

# Complete name of functions that never returns. When checking for
# inconsistent-return-statements if a never returning function is called then
# it will be considered as an explicit return statement and no message will be
# printed.
never-returning-functions=sys.exit,argparse.parse_error


[STRING]

# This flag controls whether inconsistent-quotes generates a warning when the
# character used as a quote delimiter is used inconsistently within a module.
check-quote-consistency=no

# This flag controls whether the implicit-str-concat should generate a warning
# on implicit string concatenation in sequences defined over several lines.
check-str-concat-over-line-jumps=no


[CODE_STYLE]

# Max line length for which to sill emit suggestions. Used to prevent optional
# suggestions which would get split by a code formatter (e.g., black). Will
# default to the setting for ``max-line-length``.
#max-line-length-suggestions=
```