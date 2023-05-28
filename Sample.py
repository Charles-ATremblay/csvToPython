class Sample:
	def __init__(self, info_id, name, lastName, sex, age, status):
		self.info_id = info_id
		self.name = name
		self.lastName = lastName
		self.sex = sex
		self.age = age
		self.status = status

	def getInfo_id(self):
		return self.info_id

	def getName(self):
		return self.name

	def getLastName(self):
		return self.lastName

	def getSex(self):
		return self.sex

	def getAge(self):
		return self.age

	def getStatus(self):
		return self.status

	def setInfo_id(self, info_id):
		self.info_id = info_id

	def setName(self, name):
		self.name = name

	def setLastName(self, lastName):
		self.lastName = lastName

	def setSex(self, sex):
		self.sex = sex

	def setAge(self, age):
		self.age = age

	def setStatus(self, status):
		self.status = status
