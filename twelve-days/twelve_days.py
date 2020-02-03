days = ['first','second','third','fourth','fifth','sixth',
        'seventh','eighth','ninth','tenth','eleventh','twelfth']
gifts = ['twelve Drummers Drumming', 'eleven Pipers Piping', 'ten Lords-a-Leaping',
         'nine Ladies Dancing', 'eight Maids-a-Milking', 'seven Swans-a-Swimming',
         'six Geese-a-Laying', 'five Gold Rings', 'four Calling Birds',
         'three French Hens', 'two Turtle Doves', 'a Partridge in a Pear Tree']
template = 'On the {} day of Christmas my true love gave to me: {}.'

def recite(start_verse, end_verse):
    return [verse(n) for n in range(start_verse-1, end_verse)]

def verse(idx):
    return template.format(days[idx],
        ', '.join(gifts[12-idx-1:-1] + [('and ' if idx else '') + gifts[-1]]))

