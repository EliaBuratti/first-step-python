""" programming procedural """

def mean (values):

    valNum_sum_for = 0

    for val in values :
        valNum_sum_for = valNum_sum_for+val

    valMean = valNum_sum_for/len(values)

    return(valMean)

def sqrt (val):
    return val**(1/2)

def default (val=1):
    return(f'il valore scelto è: {val}')

def triangle_area (b, h):
    return b*h/2

def is_leap (year):

    leap = False


    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap = True
        else:
            leap = True

    return leap

def is_anagrams (word_first, word_second):

    if len(word_first)!=len(word_second):
        return False
    
    word_first_list = list(word_first)

    for c in word_second:
        if c in word_first_list:
            word_first_list.remove(c)
        else:
            return False
        
    return True

def validate_email(email):

    parts = email.split('@')

    if len(parts)!=2:
        return False
    
    name, parts = parts

    parts = parts.split('.')

    if len(parts)!=2:
        return False
    
    domain, ext = parts

    if not name.replace('-','').replace('_','').isalnum():
        return False
    
    if not domain.isalnum():
        return False
    
    if len(ext)>3:
        return False
    
    return True

def email_filter (emails):

    valid_email = list(filter(validate_email, emails))
    valid_email.sort()
    return valid_email

""" example to use mean"""
l = [12, 1, 23, 43, 65, 2, 11, 34]
l_mean = mean(l)
print(l_mean)


""" example to use default values """
print(default(), default(5))

""" def with mutiple values """
print(triangle_area(10, 5))

""" year leap """
year = int(input('Choose a year: '))
print('The year choice '+ ('is leap' if is_leap(year) else 'isn\'t leap'))

""" check that the words are anagrams """
word1 = input('Write a first word: ')
word2 = input('Write a second word: ')

print('The words are '+ ('anagram' if is_anagrams(word1,word2) else 'isn\'t anagram'))

""" validation email address and return correct mail and ordered by alphabetic """
emails = ['elia@example.com', 'mario$rossi@example.com', 'luigi@example.comm','giuseppeexample.com','nicola@example','marco@example.com', 'andrea@example.com']

print(email_filter(emails))