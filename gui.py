#coding=utf-8
__author__ = 'zhulixin'

# http://py.vaults.ca
# http://wiki.python.org/moin/GuiProgramming
# http://wiki.python.org/moin/TkInter
# http://wxpython.org
# http://starship.python.net/crew/mhammond
# http://pygtk.org
# http://wiki.python.org/moin/PyQt

import wx

def load(event):
    file = open(filename.GetValue())
    content.SetValue(file.read())
    file.close()

def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(content.GetValue())
    file.close()

app = wx.App()
win = wx.Frame(None, title='test window', size=(600, 200))
panel = wx.Panel(win)

filename = wx.TextCtrl(panel)
content = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)
loadButton = wx.Button(panel, label='Open')
loadButton.Bind(wx.EVT_BUTTON, load)
saveButton = wx.Button(panel, label='Save')
saveButton.Bind(wx.EVT_BUTTON, save)
hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(content, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
panel.SetSizer(vbox)
win.Show()
app.MainLoop()



