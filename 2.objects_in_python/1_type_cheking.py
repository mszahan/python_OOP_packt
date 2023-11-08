name = 'sojib'
# print(id(name))
# print(type(name))
# print(hash(name))

num = 44
# print(id(num))
# print(type(num))
# print(hash(num))

# special_str = "a%d"
# print(special_str % 113)
# print("%d")

# print(f"so the name is {name} and the number is {num} ")


def odd(n: int) -> bool:
    return n % 2 != 0


def even(n):
    n = int(n)
    return 'even number'


print(odd('hola'))
print(even(5))
