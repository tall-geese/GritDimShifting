from sqlalchemy.engine import create_engine
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import config


eng = create_engine(config.CONNECTION_STRING)

ML_Query = """

        SELECT frd.Value[Size], 'Machined'[Finish] 
        FROM MeasurLink7.dbo.Run run
        LEFT OUTER JOIN MeasurLink7.dbo.FeatureRunData frd on run.RunID = frd.RunID 
        LEFT OUTER JOIN MeasurLink7.dbo.Feature fe on fe.FeatureID = frd.FeatureID 
        WHERE run.RunName ='AL0654' and fe.FeatureName ='0_004_00'

        """

data = pd.read_sql_query(sql=ML_Query,con=eng)

data = data.append(pd.read_csv('csv/CamData from AL0654.csv'))
g = sns.histplot(data=data, x='Size', hue='Finish', bins=15, kde=True, stat='density')
plt.show()