import sys, os
from PySide6.QtGui import QIcon, QColor, QPalette, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app = QApplication(sys.argv)

palette = QApplication.palette()
theme_color = palette.color(QPalette.Highlight)

# Create an icon from a file
icon = QIcon(DIR_PATH + "/resources/images/icons8-clouds-48.png")

# Set the icon color based on the system theme color
pixmap = icon.pixmap(64, 64)
# pixmap.fill(theme_color)
icon = QIcon(pixmap)

tray_icon = QSystemTrayIcon(icon)
tray_icon.show()

sys.exit(app.exec_())
