"""
This is a small library for Natural Language Generation.

The library has some basic building blocks for creating document plans,
syntactic structures with parameters and has a simplenlg wrapper so that 
created syntactic structures can be realised using simpleNLG.

"""

import logging

logging.getLogger('nlg').info('initialising NLG library')

from .pipeline import Pipeline