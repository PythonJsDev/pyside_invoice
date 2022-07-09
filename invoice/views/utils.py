from PySide6 import QtWidgets


def separator_hline(self, name: str = 'Hline', thick: int = 1):
    self.separator_line = QtWidgets.QFrame()
    self.separator_line.setFrameShape(QtWidgets.QFrame.HLine)
    self.separator_line.setLineWidth(thick)
    self.separator_line.setObjectName(name)
    return self.separator_line


def doc():
    print('doc')


def check_len_data(self, len_data):
    for d in len_data:
        data = d[0]
        length = d[1]
        message = d[2]
        if not len(data) or len(data) < length:
            QtWidgets.QMessageBox.warning(self, 'Erreur', message)
            return False
    return True


def check_email(self, email):
    if not email or email.count('@') == 1:
        return True
    QtWidgets.QMessageBox.warning(self, 'Erreur', 'email invalide')
    return False
