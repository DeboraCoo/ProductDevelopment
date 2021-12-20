#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = []

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = []


#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Income']

DROP_FEATURES = ['Dt_Customer', 'Marital_Status','MntMeatProducts']

#Variables para binarización por sesgo fuerte
BINARIZE_VARS = ['MntWines','MntFruits','MntFishProducts','MntSweetProducts']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['Education' ]

#Variables seleccionadas según análisis de Lasso
FEATURES = [
    'ID', 'Education', 'Marital_Status', 'Income', 'Kidhome', 'Teenhome',
       'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts',
       'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
       'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
       'NumStorePurchases', 'NumWebVisitsMonth','Dt_Customer'
]