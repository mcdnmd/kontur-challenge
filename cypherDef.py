import string


def solve_cypher(question):
	if question.find("Caesar's code") >= 0:
		return solve_cypher_caesar(question, "cypher")
	elif question.find("first longest word") >= 0:
		return "continue"
	else:
		return "continue"

def solve_cypher_caesar(question, type_t):
	alph = string.digits + '-'

	alph_all = ""
	if type_t == "cypher":
		alph_all = " " + string.ascii_lowercase + string.digits + "\'"
		checker = False
	elif type_t == "determinant" or type_t == "inverse-matrix":
		alph_spec = " &-0123456789\\"
		checker = True
	elif type_t == "poly":
		alph_spec = " ()*+-.0123456789^x"
		checker = True
	elif type_t == "cypher_json":
		alph_spec = " abcdefghijklmnopqrstuvwxyz0123456789'-"
		checker = True

	answer = []
	code = ""
	ans = ""
	n = len(question)
	

	j = 14
	while question[j] in alph:
		code += question[j]
		j += 1

	question = question[j+1:]
	#print(question[5])
	if checker:
		j = 4
		while question[j] in alph_spec:
			alph_all += question[j]
			j += 1
		p = j
		question = question[p+1:]

	#print(alph_all)
	numOfChar = len(alph_all)
	n = len(question)
	for i in range(n):
		index = (alph_all.index(str(question[i])) - int(code)) % (numOfChar)
		answer.append(alph_all[index])

	for i in range(len(answer)):
		ans += answer[i]

	value = ans

	return value

