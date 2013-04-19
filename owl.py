#!/usr/bin/env python
# encoding:UTF-8

"""
Created on Dec 28, 2011

@author: Sean Buscay
"""

# Import Python Core Modules
import uuid
import time

# Import tablib @see https://github.com/kennethreitz/tablib
import tablib

from maclib import activewindow, idledetect


class OwlApp():
    def __init__(self):

        # Define log file.
        self.log_file = 'logs/' + time.strftime("%Y-%b-%d-%H-%M-%S", time.localtime())

        global data
        data = tablib.Dataset()
        data.headers = ['id', 'window_text', 'application_name', 'window_name', 'start', 'stop', 'seconds',
                        'greatest_idle_time']

        # Define initial variable values.
        self.id = str(uuid.uuid4())
        self.window_text = 'Owl Timer, Startup'
        self.application_name = 'Owl Timer'
        self.window_name = 'Startup'
        self.start = self.now()
        self.stop = self.now()
        self.seconds = 1
        self.greatest_idle_time = 1

        self.append_entry()

        self.set_fresh_variables()

    # Logic in this function keeps it from logging an entry every second.
    # Instead it keeps track of the greatest idle time in between logging events,
    # tracks when the app window first went active, and writes tracking data upon 
    # change to next window.

    def log(self):

        # If the time since the last user input (idle duration) is greater than the time in the
        # greatest_idle_time variable, the greatest_idle_time value gets set to the greater system 
        # idle duration returned by idledetect.get_idle_duration().
        if idledetect.get_idle_duration() > self.greatest_idle_time:
            self.greatest_idle_time = idledetect.get_idle_duration()

        # If the window text being tracked is not the text returned by get_activeWindowName
        # then a new window is active.
        if self.window_text != activewindow.get_activeWindowName():
            self.seconds = self.time_stamp() - self.start_time_stamp

            self.append_entry()

            with open(self.log_file+'.json', 'wb') as f:
                f.write(data.json)

            with open(self.log_file+'.xls', 'wb') as f:
                f.write(data.xls)

            self.set_fresh_variables()

    def append_entry(self):
        data.append(
            [self.id, self.window_text, self.application_name, self.window_name, self.start, self.stop, self.seconds,
             self.greatest_idle_time])

    def set_fresh_variables(self):

        self.start_time_stamp = self.time_stamp()

        # Add values for logged variables.
        self.id = str(uuid.uuid4())
        self.window_text = activewindow.get_activeWindowName()
        self.application_name = activewindow.get_applicationName(self.window_text)
        self.window_name = activewindow.get_windowName(self.window_text)
        self.start = self.now()
        self.stop = self.now()
        self.seconds = 0
        self.greatest_idle_time = 0

    def time_stamp(self):
        return int(time.time())

    def now(self):
        return time.strftime("%d %b %Y - %H:%M:%S")


if __name__ == '__main__':

    app = OwlApp()

    while True:
        time.sleep(1)
        app.log()