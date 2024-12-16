import flet as ft

class CustomTab(ft.Control):
    def __init__(self, title, content_text, sub_menu_items, page):
        super().__init__()
        self.title = title
        self.content_text = content_text
        self.sub_menu_items = sub_menu_items
        self.page = page
        self.is_active = False
        self._build()

    def _build(self):
        self.tab_button = ft.TextButton(
            text=self.title,
            on_click=self.switch_tab,
            style=ft.ButtonStyle(
                color={"hovered": ft.Colors.BLUE},
                bgcolor={"active": ft.Colors.BLUE_100}
            )
        )
        
        # Divide the sub-menu items into rows of four buttons each
        rows = []
        for i in range(0, len(self.sub_menu_items), 4):
            row_items = self.sub_menu_items[i:i+4]
            rows.append(ft.Row(row_items, alignment=ft.MainAxisAlignment.START))
        
        self.sub_menu_rows = rows
        
        for row in self.sub_menu_rows:
            row.visible = self.is_active
        
        # Create the content text control
        self.content_label = ft.Text(value=self.content_text, expand=True)
        
        self.container = ft.Container(
            content=ft.Column([*self.sub_menu_rows, self.content_label], expand=True),
            visible=self.is_active,
            expand=True
        )

    def switch_tab(self, e):
        self.is_active = not self.is_active
        for row in self.sub_menu_rows:
            row.visible = self.is_active
        self.container.visible = self.is_active
        self.content_label.visible = self.is_active
        self.update()
        self.page.update()  # Force update the entire page

    def build(self):
        return ft.Column([self.tab_button, self.container])

def main(page: ft.Page):
    # Set the page title
    page.title = "Flet Custom Desktop Application Component: Custom Ribbon Component Template"
    
    # Define button styles
    button_style = {
        "height": 40,
        "width": 100,
        "style": ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5)
        )
    }

    # Create file tab content
    file_sub_menu_items = [
        ft.TextButton(text="New", icon=ft.Icons.CREATE_NEW_FOLDER, on_click=lambda _: print("Create new file"), **button_style),
        ft.TextButton(text="Open", icon=ft.Icons.FOLDER_OPEN, on_click=lambda _: print("Open file"), **button_style),
        ft.TextButton(text="Save", icon=ft.Icons.SAVE, on_click=lambda _: print("Save file"), **button_style),
        ft.TextButton(text="Save As", icon=ft.Icons.SAVE_AS, on_click=lambda _: print("Save as file"), **button_style),
        ft.TextButton(text="Print", icon=ft.Icons.PRINT, on_click=lambda _: print("Print file"), **button_style),
        ft.TextButton(text="Export", icon=ft.Icons.IMPORT_EXPORT, on_click=lambda _: print("Export file"), **button_style),
        ft.TextButton(text="Import", icon=ft.Icons.UPLOAD_FILE, on_click=lambda _: print("Import file"), **button_style),
        ft.TextButton(text="Delete", icon=ft.Icons.DELETE, on_click=lambda _: print("Delete file"), **button_style),
    ]
    file_content_text = "This is the file page"

    # Create edit tab content
    edit_sub_menu_items = [
        ft.TextButton(text="Cut", icon=ft.Icons.CONTENT_CUT, on_click=lambda _: print("Perform cut"), **button_style),
        ft.TextButton(text="Copy", icon=ft.Icons.CONTENT_COPY, on_click=lambda _: print("Perform copy"), **button_style),
        ft.TextButton(text="Paste", icon=ft.Icons.CONTENT_PASTE, on_click=lambda _: print("Perform paste"), **button_style),
        ft.TextButton(text="Undo", icon=ft.Icons.UNDO, on_click=lambda _: print("Undo operation"), **button_style),
        ft.TextButton(text="Redo", icon=ft.Icons.REDO, on_click=lambda _: print("Redo operation"), **button_style),
        ft.TextButton(text="Find", icon=ft.Icons.SEARCH, on_click=lambda _: print("Search content"), **button_style),
        ft.TextButton(text="Replace", icon=ft.Icons.EDIT, on_click=lambda _: print("Replace content"), **button_style),  # Replace icon
        ft.TextButton(text="Select All", icon=ft.Icons.SELECT_ALL, on_click=lambda _: print("Select all content"), **button_style),
    ]
    edit_content_text = "This is the edit page"

    # Create view tab content
    view_sub_menu_items = [
        ft.TextButton(text="Zoom In", icon=ft.Icons.ZOOM_IN, on_click=lambda _: print("Zoom in view"), **button_style),
        ft.TextButton(text="Zoom Out", icon=ft.Icons.ZOOM_OUT, on_click=lambda _: print("Zoom out view"), **button_style),
        ft.TextButton(text="Full Screen", icon=ft.Icons.FULLSCREEN, on_click=lambda _: print("Toggle full screen"), **button_style),
        ft.TextButton(text="Restore", icon=ft.Icons.FULLSCREEN_EXIT, on_click=lambda _: print("Exit full screen"), **button_style),
        ft.TextButton(text="Actual Size", icon=ft.Icons.PHOTO_SIZE_SELECT_ACTUAL, on_click=lambda _: print("Actual size"), **button_style),
        ft.TextButton(text="Fit Width", icon=ft.Icons.PHOTO_SIZE_SELECT_LARGE, on_click=lambda _: print("Fit width"), **button_style),
        ft.TextButton(text="Fit Height", icon=ft.Icons.PHOTO_SIZE_SELECT_SMALL, on_click=lambda _: print("Fit height"), **button_style),
        ft.TextButton(text="Reset View", icon=ft.Icons.PAN_TOOL, on_click=lambda _: print("Reset view"), **button_style),
    ]
    view_content_text = "This is the view page"

    # Create custom tabs
    file_tab = CustomTab("File", file_content_text, file_sub_menu_items, page)
    edit_tab = CustomTab("Edit", edit_content_text, edit_sub_menu_items, page)
    view_tab = CustomTab("View", view_content_text, view_sub_menu_items, page)

    # Initialize the first tab as active
    file_tab.is_active = True
    file_tab.container.visible = True
    for row in file_tab.sub_menu_rows:
        row.visible = True
    file_tab.content_label.visible = True

    # Create the tab title bar
    tab_titles = ft.Row([
        file_tab.tab_button,
        edit_tab.tab_button,
        view_tab.tab_button,
    ], alignment=ft.MainAxisAlignment.START)

    # Create the main layout
    main_layout = ft.Column([
        tab_titles,
        ft.Divider(height=1, color=ft.Colors.GREY_300),
        ft.Column([
            file_tab.container,
            edit_tab.container,
            view_tab.container,
        ], expand=True)
    ])

    # Add the main layout to the page
    page.add(main_layout)

    # Define a method to switch tabs
    def switch_to_tab(tab):
        for t in [file_tab, edit_tab, view_tab]:
            if t == tab:
                t.is_active = True
                t.container.visible = True
                for row in t.sub_menu_rows:
                    row.visible = True
                t.content_label.visible = True
            else:
                t.is_active = False
                t.container.visible = False
                for row in t.sub_menu_rows:
                    row.visible = False
                t.content_label.visible = False
        page.update()

    # Bind the tab switching method
    file_tab.tab_button.on_click = lambda e: switch_to_tab(file_tab)
    edit_tab.tab_button.on_click = lambda e: switch_to_tab(edit_tab)
    view_tab.tab_button.on_click = lambda e: switch_to_tab(view_tab)

ft.app(target=main)