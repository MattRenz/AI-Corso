"""
Set di dati del Titanic: Si tratta di un classico dataset utilizzato nell'apprendimento 
automatico che contiene informazioni sui passeggeri che erano a bordo del Titanic, tra cui la 
loro età, il sesso e lo stato di sopravvivenza. Il dataset può essere scaricato da Kaggle e 
può essere utilizzato per operazioni di pulizia, aggregazione e trasformazione dei dati.
"""

import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

print (titanic.columns)
print(titanic.head())

print(len(titanic))
tit_without_emptyvalues = titanic.dropna()
print(len(tit_without_emptyvalues))

#converto int column to float
titanic["survived"] = pd.to_numeric(titanic["survived"], downcast="float")
print(titanic.head())



#Altri esempi
# Drop columns that are not needed for analysis
titanic = titanic.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# Fill in missing values in the Age column with the mean age
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean())

# Create a new column called "FamilySize" by adding the "SibSp" and "Parch" columns
titanic['FamilySize'] = titanic['SibSp'] + titanic['Parch'] + 1

# Create a new column called "IsAlone" that indicates whether the passenger is traveling alone or with family
titanic['IsAlone'] = 1
titanic.loc[titanic['FamilySize'] > 1, 'IsAlone'] = 0

# Map the "Sex" column to numerical values
titanic['Sex'] = titanic['Sex'].map({'male': 0, 'female': 1})

# Map the "Embarked" column to numerical values and fill in missing values with the mode
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])
titanic['Embarked'] = titanic['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Rename the "Survived" column to "Target" for clarity
titanic = titanic.rename(columns={'Survived': 'Target'})

# Preview the transformed dataset
print(titanic.head())
