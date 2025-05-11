import flet as ft

def main(page: ft.Page):
    def open_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            with open(e.files[0].path, "r", encoding="utf-8") as f:
                textfield.value = f.read()
            page.update()

    def save_file_result(e: ft.FilePickerResultEvent):
        if e.path:
            with open(e.path, "w", encoding="utf-8") as f:
                f.write(textfield.value)

    # File pickers for open/save
    open_file_picker = ft.FilePicker(on_result=open_file_result)
    save_file_picker = ft.FilePicker(on_result=save_file_result)
    page.overlay.extend([open_file_picker, save_file_picker])

    # Text area
    textfield = ft.TextField(
        multiline=True,
        min_lines=40,
        autofocus=True,
        border=ft.InputBorder.OUTLINE,
        cursor_color='yellow',
        content_padding=20,
        hint_text="Start typing...",
        expand=True,
    )

    # Buttons
    open_button = ft.ElevatedButton("📂 Open File", on_click=lambda e: open_file_picker.pick_files(allowed_extensions=["txt"]))
    save_button = ft.ElevatedButton("💾 Save File", on_click=lambda e: save_file_picker.save_file(file_name="document.txt"))

    # Layout
    page.title = "Text Editor"
    page.add(ft.Row([open_button, save_button]), textfield)

ft.app(target=main)

if __name__ == '__main__':
    import os
    ft.app(target=main, view=None, port=int(os.environ.get("PORT", 8501)))

