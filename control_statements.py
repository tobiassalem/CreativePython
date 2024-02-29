temperature = int(input('What is the current temperatures? '))

if temperature > 30:
    print("It's a hot day")
    print("Drink enough water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit chilly")
else:
    print("It's cold")
print("Done")

i = 1
while i <= 10:
    print(f'i= {i}')
    print(i * '*')
    i += 1
