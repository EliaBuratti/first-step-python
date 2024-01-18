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



