import requests
import json
import math
import string
import time
from word2number import w2n

from cypherDef import solve_cypher
from polynomialDef import solve_polynomialroot
from determinantDef import solve_determinant
from shapeDef import solve_shape
from jsonDef import solve_json
from inverseDef import solve_inverse
from mathDef import solve_math
from mathStackDef import solve_stack_math
from stringNumberDef import solve_stringNumber

#==========================================================================
team_token = 'WF60J9PQ4d9tjOS1ZVHNm2yiXtSMUk7'
url = "https://task-challenge.azurewebsites.net/api/tasks/"
print("+=========================+")
print("Client for Challenge is ON!")
print("+=========================+")

while True:
	#print("press Enter to get task")
	#input()
	print("I`ll get task after 2 sec")
	time.sleep(1)
#==========================================================================
	response = requests.post(url, params={'secret':team_token, 'round':'projects-course-4'})
	json_response = response.json()
	print("You hava a new task:")
	print(f"TaskId:		{json_response['id']}")
	print(f"TaskType:		{json_response['typeId']}")
	print(f"Question:		{json_response['question']}")
	task_type = json_response['typeId']
	question = json_response['question']
	task_id = json_response['id']
#==========================================================================

	if task_type == 'cypher':						# 1/3 Done
		value = solve_cypher(question)
		if value == "continue":
			continue
	elif task_type == 'polynomial-root':			# Done
		value = solve_polynomialroot(question)
	elif task_type == 'determinant':				# Done 
		value = solve_determinant(question)
	elif task_type == 'shape':						# Hand-made
		value = solve_shape(question)
	elif task_type == 'string-number':				# Done 
		value = solve_stringNumber(question)
	elif task_type == 'inverse-matrix':				# Done
		value = solve_inverse(question)
	elif task_type == 'json':						# Done
		value = solve_json(question)
	else:											# Done
		if question.count('i') != 0 or question.count('a') != 0 or question.count('e') != 0 or question.count('t') != 0 or question.count('o') != 0:
			value = solve_math(question)
		else:
			solve_stack_math(question)
			file = open('ans', 'r')
			value = file.read()
			file.close()


#==========================================================================
	print(f"Answer:		{value}")
	#print(f"Press Enter to send answer!")
	#input()
	print("I`m sending your answer to server!")
	print("==================================================================\n\n")
#==========================================================================
	answer = json.dumps({"answer":str(value)})
	header = {'Content-Type':'application/json'}

	response = requests.post(url + task_id, headers=header, params={'secret':team_token}, data=answer)
	json_response = response.json()
	if json_response['status'] == 1:
		print(f"Good work status was {json_response['status']}")
		print("==================================================================\n\n")
	else:
		print(f"Err0r")
		break