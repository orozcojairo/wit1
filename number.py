#print name
for x in range(10):
    print("jairo")
    print("orozco")

#numbers 1-40
for x in range(1, 41):
    print(x)

# numbers add all 1-40
y = 0
for x in range(1, 41):
    y = y + x
    print(y)

# all even number from 10-30
y = 0
for x in range(10, 31):
    if x % 2 == 0:
        print(x)

#print all odd numbers from 51-81
for x in range(51, 82):
    if x % 2 != 0:
        print(x)
