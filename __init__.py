"""
Every combination of characters in a string
by Alex Chung

Input: "abc",2,3

Output:
aa
ba
ca
ab
bb
cb
ac
bc
cc
aaa
baa
caa
aba
bba
...
ccc
"""


def scramble(_dictionary, _min, _max):
    _out = []  # Var for storing output
    _dictionary = [i for i in _dictionary]  # Convert input string to list
    _cur = ""  # Cache variable (set each loop)
    for i in range(_min):  # Setup cache variable
        _cur += _dictionary[0]
    _dest = ""  # Final aim var
    for i in range(_max):  # Setup final aim
        _dest += _dictionary[len(_dictionary) - 1]
    _out.append(_cur)  # Initial output
    _len = _min  # Var for current length of string (in chars)
    while _cur != _dest:  # Main program loop
        _test = ""  # Temp var for checking if new character needs to be added
        for i in range(_len):
            _test += _dictionary[len(_dictionary) - 1]
        if _cur == _test:  # Character needs to be added
            _cur = ""
            _len += 1
            for i in range(_len):
                _cur += _dictionary[0]
        else:  # Character doesn't need to be added
            _ind = 0
            _count = 0
            for i in _cur:  # Determine index of character that needs to be ticked up
                if i != _dictionary[len(_dictionary) - 1]:
                    _ind = _count
                    break
                _count += 1
            _cur = _cur[:_ind] + _dictionary[_dictionary.index(_cur[_ind]) + 1] + _cur[_ind + 1:]  # Tick character
            for i in range(_ind):  # Reset characters before one just ticked for next round
                _cur = _cur[:i] + _dictionary[0] + _cur[i + 1:]
        _out.append(_cur)  # Add to output
    return _out


_result = scramble(input("Character set (no repeats): "), int(input("Minimum characters (inclusive): ")),
                   int(input("Maximum characters (inclusive): ")))
_choice = int(input("Done.\n1) Show results in one line\n2) Show results on individual lines\n3) Exit\nChoice: "))
if _choice == 1:
    print(_result)
elif _choice == 2:
    for i in _result:
        print(i)
