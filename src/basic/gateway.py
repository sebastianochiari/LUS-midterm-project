"""
Python script to check the inputs passed by the Makefile to train.sh
"""

import os
import sys

# read parameters and check for validity:
#1) n-gram order
#2) ['witten_bell' | 'absolute' | 'katz' | 'kneser_ney' | 'presmoothed' | 'unsmoothed']
#3) cutoff value (optional)

# CASE: less than two parameters specified
if( len(sys.argv) < 3 ):
    print("Wrong usage. Please specify: \n - order: n-gram order (integer number) \n - method: ['witten_bell' | 'absolute' | 'katz' | 'kneser_ney' | 'presmoothed' | 'unsmoothed'] \n - cutoff: (optional) integer number")
    raise SystemExit

order = sys.argv[1]
method = sys.argv[2]

# CASE: ORDER parameter not an integer
if( not(isinstance(order, int)) ):
    print('Wrong usage. You specified an illegal ordering type. The n-gram order parameter must be an integer number')
    raise SystemExit

# CASE: METHOD parameter not string
if( not(isinstance(method, str)) ):
    print('Wrong usage. You specified an illegal method type. The method parameter must be a string')
    raise SystemExit

# CASE: METHOD parameter not from the methods list
if( not(sys.argv[3] in ['witten_bell','absolute','katz','kneser_ney','presmoothed','unsmoothed']) ):
    print('Wrong usage. The specified "method" is not valid. The valid methods are the following: \n ["witten_bell" | "absolute" | "katz" | "kneser_ney" | "presmoothed" | "unsmoothed"] ')
    raise SystemExit

# CASE: if CUTOFF parameter specified
if( len(sys.argv) == 4):
    cutoff = sys.argv[3]
    # CASE: CUTOFF parameter not an integer
    if( not(isinstance(cutoff, int)) ):
        print('Wrong usage. You specified an illegal cutoff parameter. The cutoff parameter must be an integer number')
        raise SystemExit