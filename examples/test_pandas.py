import pandas as pd
import numpy as np

print pd.__version__

cities = pd.Series(['Mumbai', 'Pune', 'Solapur', 'Mumipur'])
population = pd.Series([435435435, 4635234, 15436, 756753])

cities_info = pd.DataFrame({'City names': cities, 'Population': population})
print cities_info

california_housing_data = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
print california_housing_data.describe()
print california_housing_data.head()
print california_housing_data.hist('housing_median_age')


print np.log(population)
print population.apply(lambda val: val > 100000)

cities_info['Area square miles'] = pd.Series([34.435, 54.23, 23.54, 78.67])
cities_info['Population Density'] = cities_info['Population']/cities_info['Area square miles']
print cities_info

print cities_info['Area square miles'].apply(lambda val: val > 50)
print cities_info['City names'].apply(lambda name: name.startswith('Mum'))

print cities.index
print cities.reindex([3,1,2,0])
print cities.reindex(np.random.permutation(cities.index))
print cities.reindex([4, 3, 1, 5, 2, 0])
