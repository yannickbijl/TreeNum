import sys
import math

import wx

from ESC_TreeNumber import ESC_TreeNumber
from GUI_TreeNumber import GUI_TreeNumber

class TreeNum(wx.Frame):
    def __init__(self, s_parent, s_title="TreeNum"):
        wx.Frame.__init__(self, s_parent, title=s_title, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self)
        box = wx.BoxSizer()
        box2 = wx.BoxSizer()
        self.treegui = GUI_TreeNumber(self.panel)
        box2.Add(self.treegui, 1, wx.ALL | wx.EXPAND)
        self.panel.SetSizer(box2)
        self.binder()
        self.Show(True)
        self.Centre()
        self.SetSize((250, 250))
        box.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)

    def binder(self):
        self.treegui.stop.Bind(wx.EVT_BUTTON, self.quitting)
        self.treegui.calc.Bind(wx.EVT_BUTTON, self.calculate)
        
    def quitting(self, event):
        sys.exit()
    
    def calculate(self, event):
        calc = ESC_TreeNumber(self.treegui.n.GetValue())
        self.treegui.unrooted.SetLabel("Unrooted trees:  " + calc.unrooted())
        self.treegui.rooted.SetLabel("Rooted trees:      " + calc.rooted())

# Is called when this script is used as the MAIN.
if __name__ == "__main__":
    class MyApp(wx.App):
        def OnInit(self):
            frame = TreeNum(None)
            frame.Show(True)
            frame.Centre()
            self.SetTopWindow(frame)
            return True

    # The application-loop
    app = MyApp(0)
    app.MainLoop()
