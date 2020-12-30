import sys

import reader2

r = reader2.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()