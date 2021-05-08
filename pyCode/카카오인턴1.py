def solution(s):
    word_num = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    for word in word_num:
        if word in s :
            s = s.replace(word, word_num[word])
    return int(s)


print(solution('one4seveneight'), '1478')
print(solution('23four5six7'), '234567')
print(solution('2three45sixseven'), '234567')
print(solution('123'), '123')
