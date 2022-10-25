import pandas as pd

data = pd.read_csv("assets/titanic.csv")
data.drop(label=['PassengerId','Name','Ticket','Cabin'], axis = 1)

sex_ = {'male':1, 'female':0}
data['Sex'].replace(sex_, inplace=True)
embarked_ = {'C':1, 'Q':2, 'S':3}
data['Embarked'].replace(embarked_, inplace=True)
