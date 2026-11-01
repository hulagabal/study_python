 
def handle_dialog(dialog, captured_messages):
        captured_messages.append(dialog.message)
        dialog.accept()
        