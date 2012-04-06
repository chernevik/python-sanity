#/usr/bin/python
# -*- coding: utf-8

#=============================================================================
"""
DESCRIPTION

Ingests a file or string specifying a test and maps the data to an object
supporting a test runner.

"""

#=============================================================================
#   Imports

import json
import os
import pdb

#=============================================================================
class Specificier(object):

    #---------------------------------------------------------------------
    def __init__(self, spec, fmt='json'):
    
        if os.path.isfile(spec):
            spec    =   open(spec, 'rb').read()

        self.json   =   json.loads(spec)
        self.d      =   json.loads(spec)

        for k, v in self.d.items():
            setattr(self, k, v)


    #---------------------------------------------------------------------

#=============================================================================
class FromDict(object):
    
    #---------------------------------------------------------------------
    def __init__(self, data):
        d = copy.deepcopy(locals)
        d.pop('self')
        for k, v in d.items():
            setattr(self, k, v)

    #---------------------------------------------------------------------

#=============================================================================
