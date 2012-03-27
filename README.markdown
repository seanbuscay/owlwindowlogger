# owlwindowlogger -- An active window logger. 
Built in Python. Logs to JSON.
=============================================================================

## PURPOSE

The purpose of the OWL Window Logger is to help people who work mostly on 
computers better track what they spent their day working on.

## PROJECT TECHNICAL GOALS

1. To work on Windows, OSX, and Linux
2. To use very little memory while tracking activity. 

## DESCRIPTION

An active window logger to help track time spent working in different 
computer applications and windows. Built in Python. Logs to JSON.

* OWL is built in Python.
* Log files are written to JSON to be consumable via many systems.
* Logging may be extended to write to CSV files or other formats.

OWL tracks and logs your computer system's:

1. Active window titles
2. Start and stop times when windows become active and stop being active
3. Idle time
4. Application thread names for active windows
5. Other variables through easy module extension

### Wanted

1. Testers
2. Contributers
3. Python Code Reviewers (I'm new to Python. Please critique.)

## ROADMAP

For right now, I'll just summarize the plan for OWL.

OWL will eventually be part of a larger system for people to accurately record 
and analyze what projects and activities they worked in a given time period.  

OWL is part one of a two part software set that is a combination desktop client 
which records activity and sends logged data to a rich internet application 
component that provides data analysis computation and end user report viewing.

Part 2 (a rich internet application component) is a long way off.    

Until then, next steps include:

1. basic analysis tools to summarize and review activity from day to day
2. porting OWL to OSX and Linux
3. testing and debugging
4. packaging for easy distribution

## STATUS

-- It's a mature alpha.

* Works on Windows
* Coding for Linux and OSX are next.

## INSTALLATION

* Installation is not hard, but it's not automatic yet.  
* For Python programmers it will be easy.  
* For programmers it should be pretty basic.  You'll need to install some stuff.
* For non-programmers or non-major techies: We'll have an installer soon.

### Windows

**Step 1:** Clone or download the OWL project from: 

https://github.com/seanbuscay/owlwindowlogger

    git clone git@github.com:seanbuscay/owlwindowlogger.git
    
**Step 2:** Create a folder called, "logs" in the project folder.  

Make sure Python has permission to write to it.

Note: Anything in the logs directory is ignored by git so you can commit changes
without sending your log data by accident.  

The following need installed on your system if they are not already:

1. Python 2.7x  -http://www.python.org/getit/
2. wxPython -http://www.wxpython.org/download.php
3. Win32 -http://starship.python.net/~skippy/win32/Downloads.html
4. psutil -http://code.google.com/p/psutil/wiki/Documentation#Classes

* (Optional) simplejson -https://github.com/simplejson/simplejson

#### Python Modules used:

1. wx
1. uuid
1. win32gui
1. time
1. json (or simplejson)
1. psutil
1. win32process

## CONTRIBUTE

If you'd like to hack on OWL, start by forking the repo on GitHub:

https://github.com/seanbuscay/owlwindowlogger

The best way to get your changes merged back into core is as follows:

1. Clone down your fork
1. Create a thoughtfully named topic branch to contain your change
1. Hack away
1. If you are adding new functionality, document it in the README
1. If necessary, rebase your commits into logical chunks, without errors
1. Push the branch up to GitHub
1. Send a pull request to the github/owlwindowlogger project.

## CREDITS

Code samples and posts that have helped in developing OWL Window Logger:

* The code that helped get me started:
-http://scott.sherrillmix.com/blog/programmer/active-window-logger/
* The gollum project readme file which helped write this readme doc. 
-https://raw.github.com/github/gollum/master/README.md
-https://github.com/github/gollum
