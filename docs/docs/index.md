# Home

Senchar is python package used for characterization of scientific image sensors such as CCDs and CMOS imagers. It is based on, but independent from, the [azcam](https://azcam.readthedocs.io/) package developed at the University of Arizona [Imaging Technology Laboratory](https://www.itl.arizona.edu/).

## Installation

```shell
pip install senchar
```

## Links

  - Main links
    - [senchar documentation (this site)](https://senchar.readthedocs.io)
    - [GitHub repo](https://github.com/mplesser/senchar)

  - Code details and links
    - [Classes](classes.md)
    - [Commands](commands.md)
    - [Code Docs](autocode.md)
    - [Advanced concepts](advanced.md)

## Scripts
Scripts are functions contained in python code modules of the same name. They may be loaded automatically during enviroment configuration and can be found in the `db.scripts` dictionary. An example script to measure system pressures might be:

```python
plot_images("/data")
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
