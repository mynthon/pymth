# -*- coding: utf8 -*-

import codecs
import translitdict

_translit_dict = {}

def prepareVal(value):
    value = value.strip()
    if value.startswith("'") and value.endswith("'") and len(value) >= 2:
        if len(value) == 2:
            value = ''
        else:
            value = value[1:-1]
    return value

def prepareDict():
    fp = codecs.open('dict.txt', 'rb', 'utf8')
    _can_scan = False
    for line in fp:

        line = line.strip()
        if not _can_scan:
            if line == '#-*-DICT-*-':
                _can_scan = True
            continue;

        if line == '':
            continue
        if line.startswith('#'):
            continue

        key, value = line.split('->')

        key = prepareVal(key)
        if key == '':
              continue

        value = prepareVal(value)


        _translit_dict[key] = value


def transliterate(val):
    out = []
    for l in val:
        out.append(translitdict.translit_dict.get(l,l))
    return ''.join(out)

print(transliterate(u'Zażółć gęślą jaźń'))
