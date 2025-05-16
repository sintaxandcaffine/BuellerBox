"""
selector_ui.py
--------------
GUI with checkboxes to let user choose from a list of Chrome tabs.

Author: SinTaxAndCaffeine
"""

import customtkinter as ctk

def prompt_user_to_select_tabs(tab_list):
    selected = []

    def on_submit():
        for i, var in enumerate(checkbox_vars):
            if var.get():
                selected.append(tab_list[i])
        root.destroy()

    root = ctk.CTk()
    root.title("🧠 Select Tabs for Bueller to Capture")
    root.geometry("700x400")

    frame = ctk.CTkScrollableFrame(root, width=680, height=340)
    frame.pack(padx=10, pady=10)

    checkbox_vars = []
    for tab in tab_list:
        var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(frame, text=f"{tab['title']} - {tab['url'][:70]}...", variable=var).pack(anchor='w')
        checkbox_vars.append(var)

    ctk.CTkButton(root, text="Capture Selected Tabs", command=on_submit).pack(pady=10)

    root.mainloop()
    return [tab_list[i] for i, var in enumerate(checkbox_vars) if var.get()]
