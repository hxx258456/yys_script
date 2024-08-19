# from time import sleep
import win32gui
import win32con
# from pykeyboard import PyKeyboard

hwnd = win32gui.FindWindow(None, '阴阳师 - MuMu模拟器')
print(hwnd)
hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
print(hwndChild)
# 激活窗口
# win32gui.SetForegroundWindow(hwnd)
hwndEdit = win32gui.FindWindowEx(hwndChild, None, None, None)
print(hwndEdit)
win32gui.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x57, 1)
win32gui.PostMessage(hwndChild, win32con.WM_CHAR, 0x57, 1)
win32gui.PostMessage(hwndChild, win32con.WM_KEYUP, 0x57, 1)
'''
for i in range(10):
    win32gui.SendMessage(hwndChild, win32con.WM_KEYDOWN, 0x57, 0)
    win32gui.SendMessage(hwndChild, win32con.WM_CHAR, 0x57, 0)
    win32gui.SendMessage(hwndChild, win32con.WM_KEYUP, 0x57, 0)
    sleep(1)
'''

# k = PyKeyboard()
# k.tap_key('w')
# win32con.VK_F11
# 0x57
# 新标签页 - Google Chrome
# win32gui.SendMessage(hwndChild, win32con.WM_SYSCOMMAND, win32con.SC_CLOSE, 0)
