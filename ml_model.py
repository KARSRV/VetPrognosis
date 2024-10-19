import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier, VotingClassifier
from sklearn.impute import SimpleImputer
from sklearn import tree

# Initialize the imputer
imputer = SimpleImputer(strategy='constant', fill_value=0)

# Initialize the classifiers with pipelines
dt_classifier = Pipeline([
    ('imputer', imputer),
    ('scaler', StandardScaler()),
    ('decision_tree', tree.DecisionTreeClassifier())
])

rf_classifier = Pipeline([
    ('imputer', imputer),
    ('scaler', StandardScaler()),
    ('random_forest', RandomForestClassifier(n_estimators=100, random_state=42))
])

gb_classifier = Pipeline([
    ('imputer', imputer),
    ('scaler', StandardScaler()),
    ('gradient_boosting', HistGradientBoostingClassifier())
])

# Voting Classifier
voting_clf = VotingClassifier(
    estimators=[
        ('decision_tree', dt_classifier),
        ('random_forest', rf_classifier),
        ('gradient_boosting', gb_classifier)
    ],
    voting='hard'
)

# Load your training dataset, replace 'cow_train.csv' with the path to your dataset
df_train = pd.read_csv('app\cow_train.csv')
X_train = df_train.drop(columns=['prognosis'])
y_train = df_train['prognosis']

# Train the model
voting_clf.fit(X_train, y_train)


def predict_disease_cow(symptom_data):
    # Ensure symptom_data has all the features that X_train has
    all_symptoms = X_train.columns.tolist()

    # Initialize a dictionary with all symptoms set to 0 (indicating absence)
    complete_symptom_data = {symptom: 0 for symptom in all_symptoms}

    # Update the symptoms that are present in the provided data
    complete_symptom_data.update(symptom_data)
    
    # Convert complete_symptom_data to a DataFrame
    input_features = pd.DataFrame([complete_symptom_data], columns=all_symptoms)
    
    # Make the prediction using the trained voting classifier
    prediction = voting_clf.predict(input_features)
    
    return prediction[0]
