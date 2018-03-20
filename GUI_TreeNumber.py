import wx


class GUI_TreeNumber(wx.Panel):
    def __init__(self, bb_parent):
        def explain():
            text = ("Calculates the number of possible unrooted and rooted" +
                    "trees. Fill in the number of organisms and press " +
                    "calculate.")
            return text
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)

        # Input Parameters
        self.n = wx.SpinCtrl(self, min=1, max=20, initial=3)
       
        # Output Parameters
        self.unrooted = wx.StaticText(self, label="")
        self.rooted = wx.StaticText(self, label="")

        # Buttons
        self.calc = wx.Button(self, label="Calculate")
        self.stop = wx.Button(self, label="Quit")
        
        # Placing of items in frame
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.StaticText(self, label=explain()), 2, wx.EXPAND | wx.ALL)
        box.Add(wx.StaticText(self, label="Number of Organisms:"), 1,
                wx.EXPAND | wx.ALL)
        box.Add(self.n, 1, wx.EXPAND | wx.ALL)
        box.Add(self.calc, 1, wx.EXPAND | wx.ALL)
        box.Add(self.unrooted, 1, wx.EXPAND | wx.ALL)
        box.Add(self.rooted, 1, wx.EXPAND | wx.ALL)
        box.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)


if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_TreeNumber"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(250, 250))
            panel = wx.Panel(self)
            panel1 = GUI_TreeNumber(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()
    
