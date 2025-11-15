name = input('enter your name: ')

vowels = 'aeiou'

count = 0
for letter in name:
    if letter in vowels:
        count = count + 1
print(count)
