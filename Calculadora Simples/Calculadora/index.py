import operator

dict_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
print("Digite um numero")
numero1 = int(input())

print("Operador")
operator = input()

print("Digite um numero")
numero2 = int(input())

print(dict_operator[operator](numero1, numero2))
