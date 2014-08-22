# -*- coding: utf-8 -*-

import unicodedata

def normalize_ascii(value):
    return unicodedata.normalize('NFKD', unicode(value))\
        .encode('ascii', 'ignore')
