import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
from portifoli import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.abrir_github)
        self.ui.pushButton_2.clicked.connect(self.abrir_linkedin)
        self.ui.pushButton_3.clicked.connect(self.abrir_whatsapp)

    def abrir_github(self):
        github_link = "https://github.com/byjulie0"
        webbrowser.open(github_link)

    def abrir_linkedin(self):
        linkedin_link = "https://www.linkedin.com/in/julie-vieira-martins-670545254"
        webbrowser.open(linkedin_link)

    def abrir_whatsapp(self):
        whatsapp_link = "https://wa.me/67991956613"
        webbrowser.open(whatsapp_link)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())