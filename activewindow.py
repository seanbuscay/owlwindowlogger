'''
Created on Apr 14, 2013

@author: buscay
'''
import applescript

script = """
global frontApp, frontAppName, windowTitle

set windowTitle to ""
tell application "System Events"
    set frontApp to first application process whose frontmost is true
    set frontAppName to name of frontApp
    tell process frontAppName
        tell (1st window whose value of attribute "AXMain" is true)
            set windowTitle to value of attribute "AXTitle"
        end tell
    end tell
end tell

return {frontAppName, windowTitle}
"""


def get_activeWindowName():
    try:
        return applescript.launch_script(script)
    except applescript.AppleScriptError:
        return '{"None Active", "None Active"}'


def get_applicationName(text):
    li = prepNames(text)
    application_name = li[0].strip()
    application_name = application_name[1:-1]
    return application_name


def get_windowName(text):
    li = prepNames(text)
    window_name = li[1].strip()
    window_name = window_name[1:-1]
    return window_name


def prepNames(text):
    text = text.strip('{')
    text = text.strip('}')
    li = text.split(',')
    if len(li) < 2:
        title = '"No Title"'
        li.append(title)

    return li

