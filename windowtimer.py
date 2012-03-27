#encoding:UTF-8

'''
Created on Dec 28, 2011

@author: Sean Buscay
'''

import wx
import uuid
import idledetect
import threadname
from win32gui import GetWindowText, GetForegroundWindow
from time import strftime, localtime, time #@todo: prob remove strftime & localtime
import jsonlogwrite as logwrite
 
class TaskBarApp(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, -1, title, size=(1, 1), style=wx.FRAME_NO_TASKBAR | wx.NO_FULL_REPAINT_ON_RESIZE)
        self.ICON_STATE = 1
        self.ID_ICON_TIMER = wx.NewId()
        self.tbicon = wx.TaskBarIcon()
        icon = wx.Icon('logon.ico', wx.BITMAP_TYPE_ICO)
        self.tbicon.SetIcon(icon, 'Logging')
        self.tbicon.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)
        self.tbicon.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.OnTaskBarRightClick)
        self.Bind(wx.EVT_TIMER, self.Log, id=self.ID_ICON_TIMER)
        self.SetIconTimer()
        self.Show(True)
        self.LogFile            = 'logs/' + str(uuid.uuid4())
        self.Data               = {}
        self.SetFreshData()
        self.Data['Message'] = 'Starting a new logging session.'
        logwrite.Write(self.Data,self.LogFile)
        self.SetFreshData()
        

    
    def OnTaskBarLeftDClick(self, evt):
        if self.ICON_STATE == 0:
            self.StartIconTimer()
            icon = wx.Icon('logon.ico', wx.BITMAP_TYPE_ICO)
            self.tbicon.SetIcon(icon, 'Logging')
            self.ICON_STATE = 1
        else:
            self.StopIconTimer()
            icon = wx.Icon('logoff.ico', wx.BITMAP_TYPE_ICO)
            self.tbicon.SetIcon(icon, 'Not Logging')
            self.ICON_STATE = 0
 
    def OnTaskBarRightClick(self, evt):
        self.StopIconTimer()
        self.tbicon.Destroy()
        self.Close(True)
        self.Data['Message'] = 'Owl Timer Shutting Down.'
        logwrite.Write(self.Data,self.LogFile)
        wx.GetApp().ProcessIdle()
        wx.GetApp().Exit()
        wx.Exit()
       
    def SetIconTimer(self):
        self.icontimer = wx.Timer(self, self.ID_ICON_TIMER)
        self.icontimer.Start(1000)

 
    def StartIconTimer(self):
        try:
            self.icontimer.Start(1000)
            self.Data['Message'] = 'Starting timer.'
            logwrite.Write(self.Data,self.LogFile)
            self.SetFreshData()
        except:
            pass
 
    def StopIconTimer(self):
        try:
            self.icontimer.Stop()
            #need to refactor to have save last application vars before loging stop
            self.Data['Message'] = 'Stopping timer.'
            logwrite.Write(self.Data,self.LogFile)
            self.SetFreshData()
        except:
            pass
 
    def Log(self, evt):
      if self.Data['Idle'] <  idledetect.get_idle_duration():
         self.Data['Idle'] = idledetect.get_idle_duration()
      
      if self.Data['Idle'] >  idledetect.get_idle_duration(): #means we had activity since last
         self.Data['TotalIdle'] = self.Data['TotalIdle'] + self.Data['Idle']
         self.Data['Idle'] = 0

      if self.Data['ActiveText']  != GetWindowText(GetForegroundWindow()):
          p = threadname.get_threadname(self.Data['Active'])
          self.Data['AppThread']   = p.name 
          self.Data['AppThreadID'] = p.pid
          self.Data['WinEnd']      = self.Now()
          logwrite.Write(self.Data,self.LogFile)
          self.SetFreshData()

    def SetFreshData(self):
        self.Data.clear()
        self.Data['Active']     = GetForegroundWindow()
        self.Data['ActiveText'] = GetWindowText(self.Data['Active'])
        self.Data['Idle']       = 0
        self.Data['TotalIdle']  = 0
        self.Data['WinStart']   = self.Now()
    
    def Now(self):
        localtime = int(time()) 
        return localtime

 
class MyApp(wx.App):
    def OnInit(self):
        frame = TaskBarApp(None, -1, ' ')
        frame.Center(wx.BOTH)
        frame.Show(True)
        return True
 
def main():
    app = MyApp(0)
    app.MainLoop()
 
if __name__ == '__main__':
    main()
