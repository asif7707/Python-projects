import customtkinter as ctk
import settings


class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=settings.DARK_GRAY)
        self.pack(fill='x', pady=4, ipady=8)


class SliderPanel(Panel):
    def __init__(self, parent, text, data_var, min_value, max_value):
        super().__init__(parent=parent)

        # layout
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self, text=text).grid(column=0, row=0, sticky='w', padx=10)
        ctk.CTkLabel(self, textvariable=data_var).grid(column=1, row=0, sticky='e', padx=10)

        ctk.CTkSlider(self, fg_color=settings.SLIDER_BG, variable=data_var,
                      from_=min_value, to=max_value).grid(column=0, row=1, columnspan=2, sticky='ew', padx=5, pady=5)