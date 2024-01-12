

for x in range(0,21,4):
    print(x)

for x in range(0,20,4):
    print(x)

longest_word = "a"

for word in ["this", "list", "of", "words", "to", "try"]:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)

my_num = 1
while my_num < 10:
    my_num += 2
    print(1)

flag = False

list_of_nums = [1,3,5,7,9,11,13,17]

while not flag:
    a_num = list_of_nums.pop()
    if a_num % 3 == 0:
        flag = True

print(a_num)