""" print('hello world') """

s = {30, 20, 15, 10, 30}

subject_set = {'Italiano', 'Storia', 'Filosofia', 'Matematica'}

report = {'latino':4, 'matematica':8}

""" print(report['latino']) """


students = {
    'Giuseppe Gullo':[
        ('matematica', 9, 0),
        ('inglese', 7, 3),
        ('storia', 8.5, 6),
        ('geografia', 5, 7),
    ],
    'Antonio Barbera':[
        ('matematica', 8, 0),
        ('inglese', 3, 3),
        ('storia', 5, 6),
        ('geografia', 9, 7),
    ],
    'Mario Rossi':[
        ('matematica', 3, 0),
        ('inglese', 2, 3),
        ('storia', 10, 6),
        ('geografia', 6, 7),
    ],
}

""" print(students) """


students['albert browne'] = [
        ('matematica', 10, 0),
        ('inglese', 10, 0),
        ('storia', 10, 0),
        ('geografia', 10, 0),
]

""" print(students) """

students['albert browne'].append(('fisica', 10, 0)),
students['Antonio Barbera'].append(('fisica', 10, 0)),
students['Giuseppe Gullo'].append(('fisica', 10, 0)),
students['Mario Rossi'].append(('fisica', 10, 0)),

""" print(students),

print(students['Antonio Barbera'][0][1]), """

""" 
- if n is odd print 'weird'
- if n is draw and between 2 to 5 print 'not weird'
- if n is draw and between 6 to 20 print 'weird'
- if n is draw and greater than 20 print 'not weird'
👇🏼
 """
n = int(input('Type a integer number.'))

if n%2==1 or 6<=n<=20:
    print('weird')

elif n>20 or 2<=n<=5:
    print('not weird')


""" while loop """

valNum = [15, 23, 18, 90]
valNum_sum = 0

i = 0 

while i<len(valNum) :
    valNum_sum = valNum_sum+valNum[i]
    i+=1

print(valNum_sum)


""" for loop """

valNum_sum_for = 0

for val in valNum :
    valNum_sum_for = valNum_sum_for+val

valMean = valNum_sum_for/len(valNum)

print(valNum_sum_for, valMean)


""" range with for loop """

u = int(input('Type a integer number.'))

for i in range(u):
    print('%d is %s' % (i, 'odd' if i%2 else 'even'))

""" range with for loop and enumarate """

shopping_list = ['tofu', 'yogurt', 'milk', 'soy']

print(list(enumerate(shopping_list))) 
""" [(0, 'tofu'), (1, 'yogurt'), (2, 'milk'), (3, 'soy')] """


""" break and continue """

shopping_list_food = ['tofu', 'yogurt', 'milk', 'soy', 'cereal', 'rice']

for i, item in enumerate(shopping_list_food):

    if 'cereal' in item:
        break

    print(f'{i+1}) {item}')


for i, item in enumerate(shopping_list_food):

    if 'cereal' in item:
        continue

    print(f'{i+1}) {item}')

print('End of list')

""" potency """

p = int(input('type a number between 1 or 20'))

if p<1 or p>20:

    print('The number must be between 1 or 20!')
else:
    for i in range(p):
        print(i**2)


""" pick second number greater """

numbers=  '2 3 4 5 6 6 7 8'

numbers= numbers.split()

numbers= set(map(int, numbers))
""" 'set' is used to remove duplicate, otherwise 'list' don't remove duplicate """

for i in numbers :

    greater = 0

    for j in numbers:

        if i<j :
            greater+=1
    if greater==1:
        break
print(i)

""" other solution to ex """

numbers_1=  '2 3 4 5 6 6 7 8'

numbers_1= numbers_1.split()

numbers_1= set(map(int, numbers_1))
""" 'set' removes duplicate but lost order, otherwise 'dict.fromkeys' remove duplicate and mantain order """

numbers_1= list(numbers_1)

""" numbers_1.sort() to order asc """

""" numbers_1.sort(reverse=True) to order desc """

numbers_1.sort(reverse=True)

print(numbers_1[1])


""" class register """
""" 
example of record input:

Mario 67 80 45 75
Luigi 60 55 70 90
Pietro 67 68 70 72

 """
students_votes = {}

n = int(input('Number of student'))

""" underscore used if not want tu use index for loop """

for _ in range(n):

    record = input('Record')
    record = record.split()
    name = record[0]
    """ record[1:] used to select all values after first """
    votes = list(map(float, record[1:]))
    students_votes[name] = votes

students_name = input('Student name to calculate average')

avg = sum(students_votes[students_name])/len(students_votes[students_name])

print(f'{avg:.2f}')

""" palindrome ex """

word = input('Write a word: ')

while word!='stop':

    word_palindrome = True
    word_lenght = len(word)

    for i in range(word_lenght):

        j = word_lenght-1-i

        if word[i]!=word[j]:
            word_palindrome = False
            break
    
    if word_palindrome:
        print(f'{word} is palindrome')
    else:
        print(f'{word} it\'s not a palindrome')
    
    word = input('Write a word: ')
