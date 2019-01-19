from wx.core import wx
from scripts import config


class OriginalImagePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        img = wx.Image(config.IMAGE_PATH, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, img, size=config.IMAGE_SIZE)