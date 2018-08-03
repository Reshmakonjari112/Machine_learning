# from __future__ import print_function
from matplotlib import cm, gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset
from IPython import display

california_housing_data = pd.read_csv("https://dl.google.com/mlcc/mledu-datasets/california_housing_train.csv", sep=",")
print california_housing_data

california_housing_data = california_housing_data.reindex(np.random.permutation(california_housing_data))