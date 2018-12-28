from wx.core import wx
import configuration


class OriginalImageFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, size=(240, 260))
        x = wx.DisplaySize()[0] / 3 - self.Size[0] / 2
        y = wx.DisplaySize()[1] / 2 - self.Size[1] / 2
        self.Position = (x, y)

        img = wx.Image(configuration.IMAGE_PATH, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, img, size=configuration.IMAGE_SIZE)