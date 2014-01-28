def getProbability(boleto):

	def calcule(match, selection, kind):

		if kind == 0:
			probability = match.getOddSimple()[2]
			selection.append(match.getNombreQuini().ljust(30) + ":\t" + match.getOddSimple()[1] + "  (" + str(round(probability*100,2)) + "%)") 
		else:
			probability = match.getOddDouble()[2]
			selection.append(match.getNombreQuini().ljust(30) + ":\t" + match.getOddDouble()[1] + "  (" + str(round(probability*100,2)) + "%)")

		return probability
	
	doubles_cad = raw_input("Enter number of doubles: ")
	doubles = int(doubles_cad)

	bestProbability = 0.00
	bestSelection = []

	for i0 in range(2):
		for i1 in range(2):
			for i2 in range(2):
				for i3 in range(2):
					for i4 in range(2):
						for i5 in range(2):
							for i6 in range(2):
								for i7 in range(2):
									for i8 in range(2):
										for i9 in range(2):
											for i10 in range(2):
												for i11 in range(2):
													for i12 in range(2):
														for i13 in range(2):

															index = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13]
															double_selection = i0 + i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13

															if double_selection <= doubles:
																probability = 1
																selection = []

																for i in range(14):
																	probability = probability * calcule(boleto[i], selection, index[i])

																if probability > bestProbability:
																	bestProbability = probability
																	bestSelection = selection

	for i in range(14):
		print bestSelection[i]

	print "Probability of success: " + str(bestProbability)
