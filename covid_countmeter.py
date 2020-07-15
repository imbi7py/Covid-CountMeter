from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup as BS
import requests 
import sys 


class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		self.setWindowTitle("Python ")

		self.setGeometry(200, 100, 500, 500)

		self.UiComponents()

		self.show()

	def UiComponents(self):

		self.country = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","DR Congo","Costa Rica","Croatia","Cuba","Cyprus","Czechia","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","North Macedonia","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts & Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

		self.combo_box = QComboBox(self)

		self.combo_box.setGeometry(150, 60, 200, 50)

		self.combo_box.setFont(QFont('Times', 10))

		for i in self.country:
			i = i.upper() 
			self.combo_box.addItem(i) 

		self.combo_box.activated.connect(self.get_cases)

		self.label_total = QLabel("Total Cases ", self)

		self.label_total.setGeometry(150, 300, 200, 40)

		self.label_total.setAlignment(Qt.AlignCenter)

		self.label_total.setStyleSheet("border : 2px solid black;")

		self.label_reco = QLabel("Recovered Cases ", self)

		self.label_reco.setGeometry(150, 350, 200, 40)

		self.label_reco.setAlignment(Qt.AlignCenter)

		self.label_reco.setStyleSheet("border : 2px solid black;")

		self.label_death = QLabel("Total Deaths ", self)

		self.label_death.setGeometry(150, 400, 200, 40)

		self.label_death.setAlignment(Qt.AlignCenter)

		self.label_death.setStyleSheet("border : 2px solid black;")


	def get_cases(self):

		index = self.combo_box.currentIndex()
		country_name = self.country[index] 


		url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"

		data = requests.get(url)

		soup = BS(data.text, 'html.parser')

		cases = soup.find_all("div", class_="maincounter-number")

		total = cases[0].text

		total = total[1: len(total) - 2]

		recovered = cases[2].text


		recovered = recovered[1: len(recovered) - 1] 


		deaths = cases[1].text 


		deaths = deaths[1: len(deaths) - 1] 


		self.label_total.setText("Total Cases : " + total) 
		self.label_reco.setText("Recovered Cases : " + recovered) 
		self.label_death.setText("Total Deaths : " + deaths) 



App = QApplication(sys.argv) 


window = Window() 

window.show() 


sys.exit(App.exec()) 


