import wx


class JNDExperimentApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(JNDExperimentApp, self).__init__(*args, **kw)

        self.SetTitle("Experimento de JND con Ley de Weber")
        # Ajustamos el tamaño para acomodar el nuevo control deslizante
        self.SetSize((800, 700))

        # Panel para organizar los controles
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Deslizador para la constante de Weber
        sizer.Add(wx.StaticText(panel, label="Constante de Weber (k)"),
                  flag=wx.CENTER | wx.TOP, border=10)
        self.weber_slider = wx.Slider(
            panel, minValue=1, maxValue=100, value=10)
        sizer.Add(self.weber_slider, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=10)
        self.weber_slider.Bind(wx.EVT_SLIDER, self.update_colors)

        # Etiqueta para mostrar el valor de la constante de Weber
        self.weber_value_label = wx.StaticText(panel, label="Valor de k: 0.10")
        sizer.Add(self.weber_value_label, flag=wx.CENTER | wx.TOP, border=5)

        # Títulos y sliders de colores
        color_names = ["Rojo", "Verde", "Azul"]
        # Colores iniciales oscuros
        base_colors = [(128, 0, 0), (0, 76, 35), (0, 0, 128)]
        self.sliders_delta_I_0 = []
        self.sliders_delta_I_1 = []
        self.labels_delta_I_0 = []
        self.labels_delta_I_1 = []
        self.panels_delta_I_0 = []
        self.panels_delta_I_1 = []
        self.comparison_labels = []  # Almacena las etiquetas de comparación

        color_sizer = wx.BoxSizer(wx.HORIZONTAL)

        for i, (name, base_color) in enumerate(zip(color_names, base_colors)):
            color_column = wx.BoxSizer(wx.VERTICAL)

            # Panel Im0
            panel_Im0 = wx.Panel(panel, size=(100, 50))
            panel_Im0.SetBackgroundColour(wx.Colour(*base_color))
            color_column.Add(wx.StaticText(
                panel, label=f"{name} Im0"), flag=wx.CENTER)
            color_column.Add(panel_Im0, flag=wx.CENTER)

            # Panel delta_I_0
            panel_delta_I_0 = wx.Panel(panel, size=(100, 50))
            panel_delta_I_0.SetBackgroundColour(wx.Colour(*base_color))
            color_column.Add(wx.StaticText(
                panel, label=f"{name} delta_I_0"), flag=wx.CENTER)
            color_column.Add(panel_delta_I_0, flag=wx.CENTER)
            self.panels_delta_I_0.append(panel_delta_I_0)

            # Slider para delta_I_0
            slider_delta_I_0 = wx.Slider(
                panel, minValue=0, maxValue=100, value=0)
            color_column.Add(slider_delta_I_0, flag=wx.EXPAND |
                             wx.TOP | wx.BOTTOM, border=5)
            self.sliders_delta_I_0.append(slider_delta_I_0)
            slider_delta_I_0.Bind(wx.EVT_SLIDER, self.update_colors)

            # Panel Im1
            panel_Im1 = wx.Panel(panel, size=(100, 50))
            panel_Im1.SetBackgroundColour(wx.Colour(*base_color))
            color_column.Add(wx.StaticText(
                panel, label=f"{name} Im1"), flag=wx.CENTER)
            color_column.Add(panel_Im1, flag=wx.CENTER)

            # Panel delta_I_1
            panel_delta_I_1 = wx.Panel(panel, size=(100, 50))
            panel_delta_I_1.SetBackgroundColour(wx.Colour(*base_color))
            color_column.Add(wx.StaticText(
                panel, label=f"{name} delta_I_1"), flag=wx.CENTER)
            color_column.Add(panel_delta_I_1, flag=wx.CENTER)
            self.panels_delta_I_1.append(panel_delta_I_1)

            # Slider para delta_I_1
            slider_delta_I_1 = wx.Slider(
                panel, minValue=0, maxValue=100, value=0)
            color_column.Add(slider_delta_I_1, flag=wx.EXPAND |
                             wx.TOP | wx.BOTTOM, border=5)
            self.sliders_delta_I_1.append(slider_delta_I_1)
            slider_delta_I_1.Bind(wx.EVT_SLIDER, self.update_colors)

            # Etiquetas para mostrar el valor de delta_I_0 y delta_I_1
            label_delta_I_0 = wx.StaticText(panel, label="delta_I_0: 0")
            label_delta_I_1 = wx.StaticText(panel, label="delta_I_1: 0")
            self.labels_delta_I_0.append(label_delta_I_0)
            self.labels_delta_I_1.append(label_delta_I_1)
            color_column.Add(label_delta_I_0, flag=wx.CENTER |
                             wx.TOP, border=5)
            color_column.Add(label_delta_I_1, flag=wx.CENTER |
                             wx.TOP, border=5)

            # Etiqueta de comparación
            comparison_label = wx.StaticText(
                panel, label="delta_I_0 == delta_I_1")
            color_column.Add(comparison_label,
                             flag=wx.CENTER | wx.TOP, border=5)
            self.comparison_labels.append(comparison_label)

            color_sizer.Add(color_column, flag=wx.ALL, border=10)

        sizer.Add(color_sizer, flag=wx.ALL | wx.EXPAND, border=10)
        panel.SetSizer(sizer)
        self.base_colors = base_colors  # Guardar los colores base para referencia
        self.update_colors()

    def update_colors(self, event=None):
        # Obtener el valor de la constante de Weber
        # Convertir a un valor decimal entre 0.01 y 1.0
        k_value = self.weber_slider.GetValue() / 100

        # Actualizar la etiqueta con el valor de k
        self.weber_value_label.SetLabel(f"Valor de k: {k_value:.2f}")

        # Actualizar los colores de los paneles en función de los sliders
        for i, (slider_delta_I_0, slider_delta_I_1, label_delta_I_0, label_delta_I_1, panel_delta_I_0, panel_delta_I_1, comparison_label) in enumerate(
            zip(self.sliders_delta_I_0, self.sliders_delta_I_1, self.labels_delta_I_0,
                self.labels_delta_I_1, self.panels_delta_I_0, self.panels_delta_I_1, self.comparison_labels)
        ):
            delta_I_0_value = slider_delta_I_0.GetValue()
            delta_I_1_value = slider_delta_I_1.GetValue()

            # Actualizar etiquetas con el valor actual de delta_I_0 y delta_I_1
            label_delta_I_0.SetLabel(f"delta_I_0: {delta_I_0_value}")
            label_delta_I_1.SetLabel(f"delta_I_1: {delta_I_1_value}")

            # Base color para el ajuste del brillo
            base_color = self.base_colors[i]

            # Modificación del color según la constante de Weber y el factor de brillo
            factor_delta_I_0 = 1 + (k_value * delta_I_0_value)
            factor_delta_I_1 = 1 + (k_value * delta_I_1_value)

            adjusted_color_delta_I_0 = wx.Colour(
                min(int(base_color[0] * factor_delta_I_0), 255),
                min(int(base_color[1] * factor_delta_I_0), 255),
                min(int(base_color[2] * factor_delta_I_0), 255)
            )
            adjusted_color_delta_I_1 = wx.Colour(
                min(int(base_color[0] * factor_delta_I_1), 255),
                min(int(base_color[1] * factor_delta_I_1), 255),
                min(int(base_color[2] * factor_delta_I_1), 255)
            )

            # Asignar el color ajustado a los paneles correspondientes
            panel_delta_I_0.SetBackgroundColour(adjusted_color_delta_I_0)
            panel_delta_I_1.SetBackgroundColour(adjusted_color_delta_I_1)

            # Refrescar los paneles para mostrar el cambio
            panel_delta_I_0.Refresh()
            panel_delta_I_1.Refresh()

            # Comparación y actualización de la etiqueta con color de semáforo
            if delta_I_0_value < delta_I_1_value:
                comparison_label.SetLabel("delta_I_0 < delta_I_1")
                comparison_label.SetForegroundColour(
                    wx.Colour(0, 255, 0))  # Verde
            elif delta_I_0_value == delta_I_1_value:
                comparison_label.SetLabel("delta_I_0 == delta_I_1")
                comparison_label.SetForegroundColour(
                    wx.Colour(204, 153, 0))  # Amarillo
            else:
                comparison_label.SetLabel("delta_I_0 > delta_I_1")
                comparison_label.SetForegroundColour(
                    wx.Colour(255, 0, 0))  # Rojo


if __name__ == "__main__":
    app = wx.App(False)
    frame = JNDExperimentApp(None)
    frame.Show()
    app.MainLoop()
