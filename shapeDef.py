import matplotlib.pyplot as plt

def solve_shape(question):
	index = question.index('|')
	tmp_array = question[index + 1:]
	coordinates = tmp_array.replace('(', '').replace(')','').split()

	xArray = []
	yArray = []

	n = len(coordinates)
	for i in range(n):
		coordinates[i] = list(map(int, coordinates[i].split(',')))
		xArray.append(coordinates[i][0])
		yArray.append(coordinates[i][1])

	plt.scatter(xArray, yArray)

	plt.show(block=False)

	print("choose 1)ellipse 2)rectangle 3)triangle 4)noise")
	ans = int(input())
	if ans == 1:
		ans = "ellipse"
	elif ans == 2:
		ans = "rectangle"
	elif ans == 3:
		ans = "triangle"
	else:
		ans = "noise"
	plt.close()
	return ans