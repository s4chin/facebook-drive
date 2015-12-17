import time

import wx

class LoginPage(wx.Frame):
    """
    Takes username and password
    """
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
    # Insert login page here

def show_splash():
    # create, show and return the splash screen
    bitmap = wx.Bitmap('WX.jpg')
    splash = wx.SplashScreen(bitmap, wx.SPLASH_CENTRE_ON_SCREEN|wx.SPLASH_NO_TIMEOUT, 0, None, -1)
    splash.Show()
    return splash

def main():
    app = wx.PySimpleApp()
    splash = show_splash()
    time.sleep(2)
    splash.Destroy()
    frame = LoginPage(None, -1, "FaceDrive")
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
