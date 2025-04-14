# Home

Senchar is package used for characterization of scientific image sensors such as CCDs and CMOS imagers.

## Installation

```shell
pip install -e senchar
```

## Links

  - Main links
    - [senchar documentation (this site)](https://senchar.readthedocs.io)
    - [GitHub repos](https://github.com/mplesser)

  - Code details and links
    - [Classes](classes.md)
    - [Commands](commands.md)
    - [Code Docs](autocode.md)
    - [Advanced concepts](advanced.md)

## Scripts
Scripts are functions contained in python code modules of the same name. They may be loaded automatically during enviroment configuration and can be found in the `db.scripts` dictionary. Scripts defined on the server side are not available as remote commands. An example script to measure system pressures might be:

```python
get_pressures(2.0, "get_pressures.log", 1)
```

## Configuration Folders
There are two important folders which are defined by most environments:

  * *systemfolder* - the main folder where configuration code is located. It is often the root of the environment's python package.
  * *datafolder* - the root folder where data and parameters are saved. Write access is required. It is often similar to `/data/sytemfolder`.

## Help
senchar is commonly used with IPython.  Help is then available by typing `?xxx`, `xxx?`, `xxx??` or `help(xxx)` where `xxx` is an senchar class, command, or object instance.

## External Links

Useful external links include:
  
 * IPython <https://ipython.org>
 * Python programming language <https://www.python.org>
