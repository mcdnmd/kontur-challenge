from mathStackDef import solve_stack_math
from determinantDef import solve_determinant
from stringNumberDef import solve_stringNumber
from cypherDef import solve_cypher_caesar


def solve_json(question):

	numArray = []
	tmpNum = ""
	jsonSum = 0

	if question.find('math|') < 0 and question.find('determinant|') < 0 and question.find('string-number|') < 0 and question.find('cypher|') < 0:
		n = len(question)
		for i in range(n):
			if question[i] in "-1234567890":
				tmpNum += question[i]
			elif tmpNum != "":
				numArray.append(tmpNum)
				tmpNum = ""

		n = len(numArray)
		for i in range(n):
			jsonSum += int(numArray[i])

	elif question.find('math|') >= 0 :
		point = question.find('math|')
		while point >= 0:
			question = question[point+5:]
			tmp_str = ""
			for i in question:
				if i != '"':
					tmp_str += i
				else:
					break
			solve_stack_math(tmp_str)
			file = open('ans','r')
			numArray.append(file.read())
			file.close()
			point = question.find('math|')
	elif question.find('determinant|') >= 0:
		point = question.find('determinant|')
		while point >= 0:
			question = question[point+12:]
			tmp_str = ""
			for i in question:
				if i != '"':
					tmp_str += i
				else:
					break
			numArray.append(solve_determinant(tmp_str))
			point = question.find('determinant|')
	elif question.find('string-number|') >= 0:
		point = question.find('string-number|')
		while point >= 0:
			question = question[point+14:]
			tmp_str = ""
			for i in question:
				if i != '"':
					tmp_str += i
				else:
					break
			numArray.append(solve_stringNumber(tmp_str))
			point = question.find('string-number|')
	elif question.find('cypher|') >= 0:
		point = question.find('cypher|')
		while point >= 0:
			question = question[point+7:]
			tmp_str = ""
			for i in question:
				if i != '"':
					tmp_str += i
				else:
					break
			numArray.append(solve_stringNumber(solve_cypher_caesar(tmp_str, "cypher_json")))
			point = question.find('cypher|')

	jsonSum = 0
	for i in numArray:
		jsonSum += int(i)
	
	return jsonSum