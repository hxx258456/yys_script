import win32con
import win32gui
import yysOS


def enum_callback(hwnd, results: list):
    # results.append((hwnd, win32gui.GetClassName(hwnd), win32gui.GetWindowText(hwnd)))
    results.append((hwnd, win32gui.GetClassName(hwnd), win32gui.GetWindowText(hwnd)))


def enum_windows() -> list:
    results = []
    win32gui.EnumWindows(enum_callback, results)
    return results


def getPid() -> list:
    pyhandleList = enum_windows()
    if len(pyhandleList) == 0:
        return []
    res = []
    for hwnd, a, b in pyhandleList:
        if yysOS.Title == b:
            res.append(win32gui.GetWindow(hwnd, win32con.GW_CHILD))
    return res


def peassKey(uCmd: int, uCmd2: int):
    res = getPid()
    if len(res) == 0:
        return
    for hwnd in getPid():
        win32gui.PostMessage(hwnd, win32con.WM_CHAR, uCmd, 1)
        win32gui.PostMessage(hwnd, win32con.WM_CHAR, uCmd2, 1)


def peassOneKey(uCmd: int, resList: list) -> int:
    WinList = resList
    if len(WinList) == 0: return 1 # noqa
    for hwnd in WinList:
        win32gui.PostMessage(hwnd, win32con.WM_CHAR, uCmd, 0)
    return 0


def getPidForName(WinName: str) -> list:
    pyhandleList = enum_windows()
    if len(pyhandleList) == 0:
        return []
    res = []
    for hwnd, a, b in pyhandleList:
        if WinName == b:
            res.append(win32gui.GetWindow(hwnd, win32con.GW_CHILD))
    return res


'''
for hwnd in getPid():
    peassKey(hwnd, yysOS.N1)
    peassKey(hwnd, yysOS.N7)

for hwnd, class_name, window_text in enum_windows():
    print(f'hwnd:{hwnd}, class_name:{class_name}, window_text:{window_text}')
'''
