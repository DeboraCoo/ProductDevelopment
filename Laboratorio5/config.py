#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = []

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = ['Cabin','Embarked']


#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Age']


#Variables para binarización por sesgo fuerte
BINARIZE_VARS = ['Fare']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['Sex', 'Ticket']

#Variables seleccionadas según análisis de Lasso
FEATURES = [
    'PassengerId',  
    'Pclass',
    'Sex',  
    'Age', 
    'SibSp', 
    'Parch', 
    'Ticket', 
    'Fare',
    'Embarked',
    'Cabin'
]