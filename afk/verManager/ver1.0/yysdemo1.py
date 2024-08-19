import time, pywinauto, win32gui, win32con, win32api

testkey = '新标签页 - Google Chrome'

hwndmain = win32gui.FindWindow(None, testkey)
hwndChild = win32gui.GetWindow(hwndmain, win32con.GW_CHILD)

app = pywinauto.application.Application().connect(handle=hwndChild)
Wizard = app[testkey]

# Wizard.send_keystrokes("{W}")

# win32gui.SendMessage(hwndChild, win32con.WM_CHAR, 0x57, 0)
temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x57, 0)
print(hwndmain)
print(hwndChild)
# 阴阳师 - MuMu模拟器
# 167-820.TXT - 记事本

# window_id = win32gui.FindWindow(None, "阴阳师 - MuMu模拟器")
# print(window_id)
# win32gui.EnumChildWindows(window_id, send_page_down, '阴阳师 - MuMu模拟器')
