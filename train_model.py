import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("C:\\Users\\Sweetlin Golda\\Desktop\\CrimePredictAI\\dataset\\crime_dataset_india.csv")

# Select required columns
df = df[['City','Time of Occurrence','Victim Age','Victim Gender','Weapon Used','Police Deployed','Crime Description']]
df = df.dropna()

# 🔹 Print unique values (BEFORE encoding)
print("City values:", df['City'].unique())
print("Time values:", df['Time of Occurrence'].unique())
print("Gender values:", df['Victim Gender'].unique())
print("Weapon values:", df['Weapon Used'].unique())
print("Crime values:", df['Crime Description'].unique())

# Label Encoding
le_city = LabelEncoder()
le_time = LabelEncoder()
le_gender = LabelEncoder()
le_weapon = LabelEncoder()
le_crime = LabelEncoder()

df['City'] = le_city.fit_transform(df['City'])
df['Time of Occurrence'] = le_time.fit_transform(df['Time of Occurrence'])
df['Victim Gender'] = le_gender.fit_transform(df['Victim Gender'])
df['Weapon Used'] = le_weapon.fit_transform(df['Weapon Used'])
df['Crime Description'] = le_crime.fit_transform(df['Crime Description'])

# Features and Target
X = df[['City','Time of Occurrence','Victim Age','Victim Gender','Weapon Used','Police Deployed']]
y = df['Crime Description']

# Train Test Split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Model
model = RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42)

model.fit(X_train,y_train)

# Save model and encoders
pickle.dump(model,open("crime_model.pkl","wb"))

pickle.dump(le_city,open("le_city.pkl","wb"))
pickle.dump(le_time,open("le_time.pkl","wb"))
pickle.dump(le_gender,open("le_gender.pkl","wb"))
pickle.dump(le_weapon,open("le_weapon.pkl","wb"))
pickle.dump(le_crime,open("le_crime.pkl","wb"))

print("Model Trained Successfully")