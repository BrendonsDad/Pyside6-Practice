#VERSION1 : Just responding to the button click : syntax
"""
from PySide6.QtWidgets import QApplication, QPushButton

#The slot : responds when something happens
def button_clicked():
    print("You clicked the button, didn't you!")

app = QApplication()
button = QPushButton()

#clicked is a signal of QPushButton. It's eitted when you click 
# on the button
#You can wire a slot to the signal using the syntax below :
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#VERSION2 : SIGNALS SENDING VALUES, CAPTURE VALUES IN SLOTS
"""
from PySide6.QtWidgets import QApplication, QPushButton

#The slot : responds
def button_clicked(data):
    print("You clicked the button, didn't you! checked: ", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True) # Makes the button checkable. It's unchecked by default. 
                        # Further clicks toggle between checked ad unchecked state

#clicked is a signal of QPushButton. It's eitted when you click o the button
#You can wire a slot to the signal usig the syntax below :

button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#VERSION3: CAPTURE VALUE FROM A SLIDER - OTHER EXAMPLE

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

#The slot : responds when something happens
def respond_to_slider(data):
    print("slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#You just do the connection. The Qt system takes care of 
#   passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
