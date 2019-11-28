from word2number import w2n


def solve_math(question):
	word_number = ""
	i = 0
	while i < len(question):
		var = question[i]
		if var in 'qwertyuiopasdfghjklzxcvbnm- ':
			word_number += var
		else:
			if word_number == 'i':
				break
			if word_number != "":
				n = len(word_number)
				question = question[:i-n]+str(w2n.word_to_num(word_number))+question[i:]
				word_number = ""
				i = i - n
		i += 1

	question = question.replace('i', 'j')
	value = str(eval(question))
	value = value.replace('j', 'i')
	if value[0] == '(' and value[len(value)-1] == ')':
		value = value[1:len(value)-1]
	return value