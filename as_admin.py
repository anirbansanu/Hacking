import ctypes, os


def isAdmin():
    try:
        is_admin = (os.getuid() == 0)  # if Unis
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0  # elese if Windows
    return is_admin
