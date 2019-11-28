import string
import numpy as np
from cypherDef import solve_cypher_caesar


def solve_polynomialroot(question):
	nums = string.digits + '-' + '.'

	p = question.find("Caesar's code")
	if p >= 0:
		question = solve_cypher_caesar(question, "poly")

	coeffs = [0]*10 # массив коэфф. при х
	answer = []
	solution = []
	coeff = "" # коэфф. при x

	n = len(question)
	i = 0

	while i < n:
		if question[i] in nums:
			coeff += question[i]
		elif question[i] == '*':
			tmpFloat = float(coeff)
			coeff = ""
		elif question[i] == 'x':
			if i + 1 < n:
				if question[i + 1] == '^':
					coeffs[int(question[i + 2])] = tmpFloat
					i += 2
				else:
					coeffs[1] = tmpFloat
			else:
				coeffs[1] = tmpFloat
		i += 1
	if coeff != "":
		coeffs[0] = float(coeff)

	# Reverse list степень убывает с ростом индекса
	for i in range(len(coeffs)-1,-1,-1):
		answer.append(coeffs[i])

	# Убераем ведущие нули из массива
	checker = True
	for i in range(len(answer)):
		if answer[i] == 0 and checker:
			pointer = i
		else:
			checker = False
			solution.append(answer[i])

	roots = np.roots(solution)

	tmp = -133728
	for i in roots:
		if i.imag == 0:
			tmp = i.real

	if tmp == -133728:
		value = 'no roots'
	else:
		value = float(tmp)

	return value