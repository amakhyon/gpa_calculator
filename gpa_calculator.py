from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import PyQt5

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.create_layout()
		self.position_layout()
		self.add_functionality()

	def create_layout(self):
		self.setWindowTitle('gpa calculator')
		self.subj_num,ok = QInputDialog.getInt(self,"get subjects","enter number of subjects")
		self.input_fields = []
		self.create_input_fields(self.subj_num)
		self.submit_btn = QPushButton('done',self)
		self.result_label = QLabel('')
		self.left_layout = QVBoxLayout()
		self.right_layout = QVBoxLayout()
		self.container_layout = QHBoxLayout()
		self.main_layout = QVBoxLayout()
		
	def position_layout(self):
		self.setGeometry(100,100,500,500)
		print(int(len(self.input_fields)/2))
		self.setLayout(self.main_layout)
		for j in range(int(len(self.input_fields)/2)):
			self.left_layout.addWidget(self.input_fields[j])
		for i in range(int(len(self.input_fields)/2), int(len(self.input_fields))):
			self.right_layout.addWidget(self.input_fields[i])
		self.container_layout.addLayout(self.left_layout)
		self.container_layout.addLayout(self.right_layout)
		self.main_layout.addLayout(self.container_layout)
		self.main_layout.addWidget(self.submit_btn)
		self.main_layout.addWidget(self.result_label)
		


	def add_functionality(self):
		self.submit_btn.clicked.connect(self.calculate_total_gpa)
		self.show()
		return
	def create_input_fields(self,num):
		for i in range(num):
			self.input_fields.append(QLineEdit('subject ' + str(i + 1)))

	def calculate_total_gpa(self):
		total_gpa = 0
		for i in range(self.subj_num):
			grade = self.input_fields[i].text()
			total_gpa += self.get_single_grade(grade)
		total_gpa = round(total_gpa,2)
		total_gpa = total_gpa / self.subj_num
		self.result_label.setText('gpa = ' + str(total_gpa))

	
	def get_single_grade(self,grade):
		grade = grade.upper()
		if grade == 'A+' :
			return 4.0
		elif grade == 'A':
			return 11.5/3
		elif grade == 'A-':
			return 11/3
		elif grade == 'B+':
			return 10/3
		elif grade == 'B':
			return 9/3
		elif grade == 'B-':
			return 8/3
		elif grade == 'C+':
			return 7/3
		elif grade == 'C':
			return 6/3
		elif grade == 'C-':
			return 5/3
		elif grade == 'D+':
			return 4/3
		elif grade == 'D':
			return 3/3
		else:
			return 0.0



app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())