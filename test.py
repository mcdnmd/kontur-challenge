from cypherDef import solve_cypher
from polynomialDef import solve_polynomialroot
from determinantDef import solve_determinant
from jsonDef import solve_json
from inverseDef import solve_inverse
from shapeDef import solve_shape
from mathDef import solve_math
from stringNumberDef import solve_stringNumber
from mathStackDef import solve_stack_math

from word2number import w2n

data = input()

#print(solve_cypher(data))

#print(solve_polynomialroot(data))

#print(solve_determinant(data))

#print(solve_json(data))

#print(solve_inverse(data))

#print(solve_shape(data))

#if data.count('i') != 0:
print(solve_math(data))
#else:
'''
solve_stack_math(data)
file = open('ans','r')
print(file.read())
file.close()
'''

#print(solve_stringNumber(data))
