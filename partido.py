'''
Created on 07/11/2013

@author: asketsus
'''
class Partido(object):
	"""Partido perteneciente al boleto de la Quiniela"""
	def __init__(self):
		self.__nombreQuini       = ["", ""]
		self.__nombreOdds        = ["", "", 0]
		self.__category          = ""
		self.__urlOddsportal     = ""
		self.__oddsAvg1X2        = [0, 0, 0, 0]
		self.__oddsAvgDC         = [0, 0, 0, 0]
		self.__oddsHigh1X2       = [0, 0, 0]
		self.__oddsHighDC        = [0, 0, 0]
		self.__oddSimple         = 0
		self.__optionSimple      = ""
		self.__payoutSimple      = 0
		self.__probabilitySimple = 1.00
		self.__oddDouble         = 0
		self.__optionDouble      = ""
		self.__payoutDouble      = 0
		self.__probabilityDouble = 1.00
		self.__keysimple         = ["1--","-X-","--2"]
		self.__keydouble         = ["1X-","1-2","-X2"]

	def putNombreQuini(self, local, away):
		self.__nombreQuini[0] = local
		self.__nombreQuini[1] = away

	def getTeamsQuini(self):
		teams = [self.__nombreQuini[0], self.__nombreQuini[1]]
		return teams

	def getNombreQuini(self):
		return self.__nombreQuini[0] + " - " + self.__nombreQuini[1]

	def putOddsportalData(self, local, away, category):
		self.__nombreOdds[0] = local
		self.__nombreOdds[1] = away
		self.__category = category

	def putURLOddsPortal(self, url):
		self.__urlOddsportal = url

	def getURLOddsPortal(self):
		return self.__urlOddsportal

	def getMatchnameOddsportal(self):
		return self.__nombreOdds[0] + " - " + self.__nombreOdds[1]

	def getCategory(self):
		return self.__category

	def putOdds1X2(self, oddsAvg, oddsHigh):
		self.__oddsAvg1X2 = oddsAvg
		self.__oddsHigh1X2 = oddsHigh
		self.selectOption("1X2")

	def putOddsDC(self, oddsAvg, oddsHigh):
		self.__oddsAvgDC = oddsAvg
		self.__oddsHighDC = oddsHigh
		self.selectOption("DC")

	def getOddSimple(self):
		option = []
		option.append(self.__oddSimple)
		option.append(self.__optionSimple)
		option.append(self.__probabilitySimple)
		return option

	def getOddDouble(self):
		option = []
		option.append(self.__oddDouble)
		option.append(self.__optionDouble)
		option.append(self.__probabilityDouble)
		return option

	def showSelect(self):
		print "Single most probable choice (" + self.__optionSimple + "): " + str(self.__oddSimple) + " (" + str(self.__probabilitySimple) + "%)"
		print "Double most probable choice (" + self.__optionDouble + "): " + str(self.__oddDouble) + " (" + str(self.__probabilityDouble) + "%)"

	def selectOption(self, option):
		oddSelected = 0
		optionSelected = 0

		if option == "1X2":
			odd1 = self.__oddsAvg1X2[0]
			odd2 = self.__oddsAvg1X2[1]
			odd3 = self.__oddsAvg1X2[2]
			odd1H = self.__oddsHigh1X2[0]
			odd2H = self.__oddsHigh1X2[1]
			odd3H = self.__oddsHigh1X2[2]
		else:
			odd1 = self.__oddsAvgDC[0]
			odd2 = self.__oddsAvgDC[1]
			odd3 = self.__oddsAvgDC[2]
			odd1H = self.__oddsHighDC[0]
			odd2H = self.__oddsHighDC[1]
			odd3H = self.__oddsHighDC[2]

		if (odd1 < odd2) & (odd1 < odd3):
			oddSelected = odd1
			optionSelected = 1
		elif (odd2 < odd1) & (odd2 < odd3):
			oddSelected = odd2
			optionSelected = 2
		elif (odd3 < odd1) & (odd3 < odd2):
			oddSelected = odd3
			optionSelected = 3
		elif (odd1 == odd2) & (odd1 != odd3):
			if odd1H < odd2H:
				oddSelected = odd1
				optionSelected = 1
			else:
				oddSelected = odd2
				optionSelected = 2
		elif (odd1 == odd3) & (odd1 != odd2):
			if odd1H < odd3H:
				oddSelected = odd1
				optionSelected = 1
			else:
				oddSelected = odd3
				optionSelected = 3
		elif (odd2 == odd3) & (odd1 != odd2):
			if odd2H < odd3H:
				oddSelected = odd2
				optionSelected = 2
			else:
				oddSelected = odd3
				optionSelected = 3
		else:
			if (odd1H < odd2H) & (odd1H < odd3H):
				oddSelected = odd1
				optionSelected = 1
			elif (odd2H < odd1H) & (odd2H < odd3H):
				oddSelected = odd2
				optionSelected = 2
			elif (odd3H < odd1H) & (odd3H < odd2H):
				oddSelected = odd3
				optionSelected = 3
			else:
				oddSelected = odd1
				optionSelected = 1

		if option == "1X2":
			self.__oddSimple = oddSelected
			self.__optionSimple = self.__keysimple[optionSelected-1]
			self.__probabilitySimple = 1 / oddSelected
		else:
			self.__oddDouble = oddSelected
			self.__optionDouble = self.__keydouble[optionSelected-1]
			self.__probabilityDouble = 1 / oddSelected













