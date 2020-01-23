days = ['first','second','third','fourth','fifth','sixth',
        'seventh','eighth','ninth','tenth','eleventh','twelfth']
gifts = ['twelve Drummers Drumming', 'eleven Pipers Piping',
         'ten Lords-a-Leaping', 'nine Ladies Dancing', 'eight Maids-a-Milking',
         'seven Swans-a-Swimming', 'six Geese-a-Laying', 'five Gold Rings',
         'four Calling Birds', 'three French Hens', 'two Turtle Doves',
         'and a Partridge in a Pear Tree.']

def recite(start_verse, end_verse):
    return [verse(n-1) for n in range(start_verse, end_verse+1)]

def verse(number):
    day = days[number]
    ans = 'On the ' + day + ' day of Christmas my true love gave to me: ' + \
          ', '.join(gifts[12-number-1:])
    return ans.replace('and ','') if number == 0 else ans

