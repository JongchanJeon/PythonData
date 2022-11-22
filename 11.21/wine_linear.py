import pandas as pd
red_df = pd.read_csv('C:/Users/jjc63/Desktop/python/PythonData/11.21/winequality-red.csv', sep = ';', header = 0, engine = 'python')

white_df = pd.read_csv('C:/Users/jjc63/Desktop/python/PythonData/11.21/winequality-white.csv', sep = ';', header = 0, engine= 'python')

#csv 파일 만들기
#red_df.to_csv('C:/Users/jjc63/Desktop/python/PythonData/11.21/winequality-red2.csv', index = False)
#white_df.to_csv('C:/Users/jjc63/Desktop/python/PythonData/11.21/winequality-white2.csv', index = False)

red_df.insert(0, column = 'type', value = 'red')
white_df.insert(0, column = 'type', value = 'white')

wine = pd.concat([red_df, white_df])

wine.columns = wine.columns.str.replace(' ', '_')
from scipy import stats
from statsmodels.formula.api import ols, glm
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']  
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality'] 

stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data = wine).fit()
regression_result.summary()