DIGIT_MAP = {'zero': '0',
             'one': '1',
             'two': '2',
             'three': '3',
             'four': '4',
             'five': '5',
             'six': '6',
             'seven': '7',
             'eight': '8',
             'nine': '9', }


def convert(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x


def convertWithHandlingExceptionKeyError(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f'Conversion succeeded x = {x}')
    except KeyError:
        print('Conversion failed')
        x = -1
    return x


def convertWithHandlingExceptionKeyTypeErrors(s):
    """Convert a string into an integer"""
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f'Conversion succeeded x = {x}')
    except(KeyError, TypeError):
        print('Conversion failed')
    return x


def convertWithHandlingExceptionKeyTypeErrorsImproved(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except(KeyError, TypeError):
        print('Conversion failed')
        return -1


import sys


def convertAccessingExceptionObjects(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except(KeyError, TypeError) as e:
        print(f'conversion error: {e!r}', file=sys.stderr)
        return -1


def convertAccessingExceptionObjectsReRaise(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except(KeyError, TypeError) as e:
        print(f'conversion error: {e!r}', file=sys.stderr)
        raise



from math import log


def string_log(s):
    v = convertAccessingExceptionObjects(s)
    return log(v)
