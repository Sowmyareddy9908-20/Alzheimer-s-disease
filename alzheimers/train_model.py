import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

#Example dataset
data={
    'Age':[60,65,70,75,80],
    'Memory':[3,2,2,1,3],
    'Thinking':[3,2,2,1,3],
    'Decision':[3,2,2,1,3],
    'Result':[0,1,1,1,0],
}
df=pd.DataFrame(data)
x=df[['Age','Memory','Thinking','Decision']]
y=df['Result']

model=RandomForestClassifier()
model.fit(x,y)

#Save model
with open("alzheimer_model.pkl","wb") as f:
    pickle.dump(model, f)
print("Model Saved Sucessfully")

