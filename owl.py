# encoding:UTF-8

'''
Created on Dec 28, 2011

@author: Sean Buscay
'''

# @todo: prob remove strftime & localtime
import uuid
import time
# import owl custom modules
import idledetect
import activewindow
# import as logwrite so the module can be swapped out for other logwriters
# such as:
# 1) import csvlogwrite as logwrite
# 2) import sqlitelogwrite as logwrite
import jsonlogwrite as logwrite


class OwlApp():
    def __init__(self):
        # setup logging
        self.LogFile = 'logs/' + time.strftime("%Y-%b-%d", time.localtime())
        # begin the data dictionary to be written as json entries in log
        self.Data = {}
        # call SetFreshData() to get time and any other available data
        self.SetFreshData()
        #self.Data['Message'] = 'Starting a new logging session.'
        # write a session startup entry
        #logwrite.Write(self.Data, self.LogFile)
        # most always set fresh data after logging
        #self.SetFreshData()


    # logic in this function keeps it from logging an entry every second.
    # instead it keeps adding up the idle stime
    # tracks when the app window first went active
    # writes tracking data upon change to next window
    def Log(self):
        if self.Data['Idle'] < idledetect.get_idle_duration():
            self.Data['Idle'] = idledetect.get_idle_duration()

        if self.Data['Idle'] > idledetect.get_idle_duration():  # means we had activity since last
            self.Data['TotalIdle'] = self.Data['TotalIdle'] + self.Data['Idle']
            self.Data['Idle'] = 0

        if self.Data['ActiveText'] != activewindow.get_activeWindowName():
            self.Data['WinEnd'] = self.Now()
            self.Data['date_end_time'] = time.strftime("%d %b %Y - %H:%M:%S")
            self.Data['Timestamp'] = self.Now()
            self.Data['GUID'] = str(uuid.uuid4())
            self.Data['Seconds'] = self.Data['WinEnd'] - self.Data['WinStart']
            self.Data['date_time_stamp'] = time.strftime("%d %b %Y - %H:%M:%S")
            self.Data['ApplicationName'] = activewindow.get_applicationName(self.Data['ActiveText'])
            self.Data['WindowName'] = activewindow.get_windowName(self.Data['ActiveText'])

            logData = {}
            logData['ID'] = self.Data['GUID'] = str(uuid.uuid4())
            logData['Window Text'] = self.Data['ActiveText']
            logData['Application Name'] = self.Data['ApplicationName']
            logData['Application Window Name'] = self.Data['WindowName']
            logData['Time Start'] = self.Data['date_start_time']
            logData['Time End'] = self.Data['date_end_time']
            logData['Seconds'] = self.Data['Seconds']
            logData['Idle Time'] = self.Data['TotalIdle']

            logwrite.Write(logData, self.LogFile)
            # reset data after log is written.
            self.SetFreshData()

    def SetFreshData(self):
        self.Data.clear()
        activetext = activewindow.get_activeWindowName()
        self.Data['ActiveText'] = activetext
        self.Data['Idle'] = 0
        self.Data['TotalIdle'] = 0
        self.Data['WinStart'] = self.Now()
        self.Data['date_start_time'] = time.strftime("%d %b %Y - %H:%M:%S")

    def Now(self):
        localtime = int(time.time())
        return localtime


if __name__ == '__main__':

    app = OwlApp()

    while True:
        pass
        time.sleep(1)
        app.Log()
