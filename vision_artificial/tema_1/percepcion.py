import wx


class ColorMixingApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ColorMixingApp, self).__init__(*args, **kwargs)

        self.SetTitle("Simulación de Mezcla de Colores RGB")
        self.SetSize((400, 300))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Etiquetas y sliders para cada color
        self.sliders = {}
        for color in ["Rojo", "Verde", "Azul"]:
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            label = wx.StaticText(panel, label=f"{color}:")
            slider = wx.Slider(panel, value=0, minValue=0,
                               maxValue=255, style=wx.SL_HORIZONTAL)
            slider.Bind(wx.EVT_SLIDER, self.OnSliderChange)
            hbox.Add(label, flag=wx.RIGHT, border=8)
            hbox.Add(slider, proportion=1)
            vbox.Add(hbox, flag=wx.EXPAND | wx.ALL, border=10)
            self.sliders[color] = slider

        # Panel de color resultante
        self.color_panel = wx.Panel(panel, size=(300, 100))
        self.color_panel.SetBackgroundColour(wx.Colour(0, 0, 0))
        vbox.Add(self.color_panel, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def OnSliderChange(self, event):
        # Obtener los valores de cada slider
        red = self.sliders["Rojo"].GetValue()
        green = self.sliders["Verde"].GetValue()
        blue = self.sliders["Azul"].GetValue()

        # Actualizar el color del panel
        color = wx.Colour(red, green, blue)
        self.color_panel.SetBackgroundColour(color)
        self.color_panel.Refresh()


if __name__ == "__main__":
    app = wx.App(False)
    frame = ColorMixingApp(None)
    app.MainLoop()
