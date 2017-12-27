
import pandas as pd
import numpy as np
import visuals as vs
from time import time
import matplotlib
from IPython.display import display
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

matplotlib
read_file = pd.read_csv('census.csv')
                          # sep='\t',
                          # header=None,
                          # names=['age']) #, 'message', 'list'])
# print read_file.head(
display(read_file.head(n=1))