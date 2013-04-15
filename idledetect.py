'''
Created on Dec 28, 2011

@author: Sean Buscay
'''

import Quartz.CoreGraphics

# From /System/Library/Frameworks/IOKit.framework/Versions/A/Headers/hidsystem/IOLLEvent.h
NX_ALLEVENTS = int(4294967295)  # 32-bits, all on.


def get_idle_duration():
    """Get number of seconds since last user input"""
    idle = Quartz.CoreGraphics.CGEventSourceSecondsSinceLastEventType(1, NX_ALLEVENTS)
    return idle