import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Preparación de los datos

'''Cargamos los datos y visualizamos'''
data = pd.read_csv('datasets/rest_data_us.csv')

print(data.head())
data.info()
print('> Duplicated data:', data.duplicated().sum())

'''
El nombre de las columnas está en el formato correcto, sin embargo, falta claridad en object_name y object_type. 
No se encontraron valores duplicados, pero hay algunos tipos de datos que no se encuentran en el tipo correcto y 
también nos encontramos con datos nulos en la columna `chain`. 

Cambiaremos los nombres de columnas ambiguos.
'''
data.columns = ['id', 'business_name', 'address', 'chain', 'business_type', 'number']

'''
Verificamos qué filas no tienen definida la columna cadena
'''

null_data = data[data['chain'].isna()]
print(null_data)

'''
Veamos si hay más establecimientos con el mismo nombre.
'''

data[data['business_name'].isin(null_data['business_name'])]

'''
Solo hay un establecimiento de cada negocio, por lo que es muy probable que el negocio no pertenezca a una
franquicia.

Realizando una búsqueda rápida por internet, se encontró que cada uno de los negocios ya ha cerrado, además,
se confirmó que los tres negocios no pertenecían a ninguna franquicia. Cambiamos entonces los valores nulos
a falso.
'''

data['chain'] = data['chain'].fillna('False')

'''
Ahora cambiaremos el tipo de columna `chain` a booleano.
'''

data['chain'] = data['chain'].astype('bool')

'''
Verificaremos si podemos cambiar la columna `business_type` a tipo categórico.
'''

print(data['business_type'].unique())

'''
Solo tenemos 6 categorias. Cambiamos entonces, a tipo categoría.
'''

data['business_type'] = data['business_type'].astype('category')

'''
Adicionalmente cambiaremos la columna number a un entero de 16 bits.
'''

data['number'] = data['number'].astype('int16')

## Análisis de datos

'''
Grafiquemos la proporción de tipo de negocios
'''
sns.set_palette('coolwarm')

sns.histplot(data=data['business_type'], stat='percent').set_title('Business distribution')
plt.grid()
plt.show()

data['business_type'].value_counts()