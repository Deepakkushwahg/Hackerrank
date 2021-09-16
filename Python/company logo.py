import math
import os
import random
import re
import sys
from collections import Counter

if __name__== '__main__':
    st=sorted(input())
    M=Counter(st).most_common(3)
    for i in M:
        print(*i) 
