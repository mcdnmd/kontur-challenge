from word2number import w2n

def solve_stringNumber(question):
	n = len(question)
	sing = ""
	word_sign = ""

	question = question.replace("minus",'-')
	if n > len(question):
		sign = '-'
		return solution(question, sign)
	question = question.replace("plus",'+')
	if n > len(question):
		sign = '+'
		return solution(question, sign)
	question = question.replace("times",'*')
	if n > len(question):
		sign = '*'
		return solution(question, sign)
	question = question.replace("thrice",'*2')
	if n > len(question):
		sign = '*3'
		return solution(question, sign)
	question = question.replace("twice",'*3')
	if n > len(question):
		sign = '*2'
		return solution(question, sign)
	question = question.replace("squared",'**2')
	if n > len(question):
		sign = '**2'
		return solution(question, sign)

	question = question.replace("cubed",'**3')
	if n > len(question):
		sign = '**3'
		return solution(question, sign)

	return w2n.word_to_num(question)

def solution(question, sign):
	if sign != "":
		tmp = question.split(" {} ".format(sign))
		ans = ""
		for i in range(len(tmp)):
			ans += str(w2n.word_to_num(tmp[i]))
			if i % 2 == 0:
				ans += f' {sign} '
	return eval(ans)