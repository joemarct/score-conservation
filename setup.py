#!/usr/bin/env python

from distutils.core import setup

setup(name='score_conservation',
      version='1.0',
      description='Protein residue conservation prediction',
      author='Tony Capra',
      author_email='tonyc@cs.princeton.edu',
      url='http://compbio.cs.princeton.edu/conservation/index.html',
      scripts=['scripts/score_conservation.py'],
      data_files=[
              ('src/score-conservation/matrix', ['scripts/matrix/blosum62.bla']), 
              ('src/score-conservation/distributions', ['scripts/distributions/blosum62.distribution'])
          ]
     )