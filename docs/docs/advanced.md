# Advanced

This document describes senchar installation, configuration, and programming. It is intended 
for advanced users.

## Versioning
The senchar can be found from `senchar.db.version` after importing senchar. It can also be obtained remotely `senchar.db.parameters.get_par("version")`.

## Conventions
 * Modules (files), objects (such as *controller*), command names (methods) and attributes (parameters) are all lowercase.
 * Filenames should be specified with forward slash ('/') separators, even under MS Windows. If back slashes are needed, they must be doubled as in `c:\\data`.
 * Strings must be enclosed in quotation marks, as in `parameters.get_par("imageroot")`. Quotation marks must match ('imageroot" is not acceptable). A quotation mark may be included in a string by preceding it with a backslash, as `"I am Mike\'s dog"` to generate `"I am Mike's dog"`.

## Tools
Python is an object oriented programming language and objects are used extensively in senchar. The main objects are instances of classes are are referred to as *tools*. Object-based commands provide control of all aspects of senchar. These commands (class methods) interact with hardware such as controllers, instruments, temperature controllers, and telescopes as well as with more virtual tools such as the exposures, images, databases, time, communication interfaces, etc. The command syntax is `tool.command(args)` where `tool` is the tool name (such as *controller*, *instrument*, *telescope*, etc.) and `command()` is the command. If `command()` uses arguments, they are specified as comma separated values of the appropriate type, such as `tool.command('ITL', 1.234, 45)`. For example, the command to initialize to the instrument is `instrument.initialize()` and the command to set the telescope focus may be  `telescope.set_focus(12.4)`.

## Parameters
Parameters may be read with the `senchar.db.parameters.get_par()` command and written with the `senchar.db.parameters.set_par()` command. For example, `senchar.db.parameters.get_par('imagetype')` returns the current image type.

## Logging
The `senchar.log()` function should be used for message output instead of python's `print()` function. This is important due to the multithreading nature of senchar.  The output of the `log()` function is defined in code and is typically directed to both the console and a rotating log file.

The `log()` function supports levels which determine if the logged message should actually be displayed. If the level value is greater than or equal to the value of `senchar.db.verbosity` then the message string is displayed. The default level is 1 for both `verbosity` and the `log()` command. Higher verbosity settings are intended for more detailed debug information.

It is also possible to direct logging to a web application, a syslog handler, or other applications. See <https://loguru.readthedocs.io/en/stable/index.html> and the `senchar.logger.py` code.
 
## Python
See <http://www.python.org> for all things pythonic.

## Ports
senchar reserves ten socket ports for each senchar process. The ports are used for various
server functions and may not all be needed in a specific environment. The command server port is the base port each senchar process and the remaining ports are incremented from that. The default command server port is 2402 for the first senchar process, 2412 for the second process, 2422 for the third, and so on. Complex systems often use many ports while the most basic systems may use no ports. Common port uses are:

  * command server port - 2402
  * web server port - 2403
  * logging server port - 2404
  * camera server port - 2405
  * Reserved - 2406
  * Reserved - 2407
  * Reserved - 2408
  * Reserved - 2409
  * Reserved - 2410
  * Reserved - 2411

Ports 2400 and 2401 are reserved for the *sencharmonitor* process which can monitor and control all *senchar* proceses on a single host.