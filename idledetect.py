'''
Created on Dec 28, 2011

@author: Sean Buscay
'''
import win32api

def get_idle_duration():
    
    millis = win32api.GetTickCount() - win32api.GetLastInputInfo()
    return millis / 1000.0

#Call get_idle_duration() to get idle time in seconds.