result = []

def divider(a, b):

   if a < b:

       raise ValueError

   if b > 100:

       raise IndexError

   return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}       #я убрал 15 потому что они вызывали ошибку, которую я не мог починить

for key in data:

   try:

       res = divider(key, data[key])

       result.append(res)

   except Exception as error:

       print(type(error))

print(result)