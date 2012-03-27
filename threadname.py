import psutil #http://code.google.com/p/psutil/wiki/Documentation#Classes
from win32process import GetWindowThreadProcessId

def get_threadname(HWND):
  pprocess = GetWindowThreadProcessId(HWND)
  p = psutil.Process(pprocess[1])
  return p