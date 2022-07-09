
def load_styles(app):
    with open("./invoice/statics/style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
