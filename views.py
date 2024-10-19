import os
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .forms import QuestionForm
from .rag_model import create_rag_app

# Replace with your PDF path
pdf_path = "app/co.pdf"  # Ensure this path is correct

# Initialize the RAG application with the specified PDF document
rag_app = create_rag_app(pdf_path)

def chat_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data["question"]
           
            answer = rag_app.run(question)
            return JsonResponse({"answer": answer})
    else:
        form = QuestionForm()

    return render(request, "chat.html", {"form": form})

def home(request):
    return render(request, "home.html")
from django.shortcuts import render
from .forms import SymptomForm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from django.http import JsonResponse
from django.views import View

def placeholder_view(request, param1, param2):
    
    return JsonResponse({'param1': param1, 'param2': param2})

def train_model():
    
    data = pd.read_csv("app\symptoms_data.csv")

    
    data.fillna('No Symptom', inplace=True)

    
    data_encoded = pd.get_dummies(data, columns=data.columns[1:], drop_first=True)

    
    X = data_encoded.drop('Disease', axis=1)
    y = data_encoded['Disease']

   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model



rf_model = train_model()


ALL_SYMPTOMS = [
    'Fever', 'Nasal Discharge', 'Loss of appetite', 'Weight Loss', 'Lameness',
    'Breathing Difficulty', 'Swollen Lymph nodes', 'Lethargy', 'Depression', 
    'Coughing', 'Diarrhea', 'Seizures', 'Vomiting', 'Eating less than usual', 
    'Excessive Salivation', 'Redness around Eye area', 'Severe Dehydration',
    'Pain', 'Discomfort', 'Sepsis', 'WeightLoss', 'Tender abdomen',
    'Increased drinking and urination', 'Bloated Stomach', 'Yellow gums',
    'Constipation', 'Paralysis', 'Wrinkled forehead', 'Continuously erect and stiff ears',
    'Grinning appearance', 'Stiff and hard tail', 'Stiffness of muscles', 'Acute blindness',
    'Blood in urine', 'Hunger', 'Cataracts', 'Losing sight', 'Glucose in urine',
    'Burping', 'Blood in stools', 'Passing gases', 'Eating grass', 'Scratching',
    'Licking', 'Itchy skin', 'Redness of skin', 'Face rubbing', 'Loss of Fur',
    'Swelling of gum', 'Redness of gum', 'Receding gum', 'Bleeding of gum',
    'Plaque', 'Bad breath', 'Tartar', 'Lumps', 'Swelling', 'Red bumps',
    'Scabs', 'Irritation', 'Dry Skin', 'Fur loss', 'Red patches',
    'Heart Complication', 'Weakness', 'Aggression', 'Pale gums',
    'Coma', 'Collapse', 'Abdominal pain', 'Difficulty Urinating', 'Dandruff',
    'Anorexia', 'Blindness', 'Excess jaw tone', 'Urine infection',
    'Lack of energy', 'Smelly', 'Neurological Disorders', 'Eye Discharge',
    'Loss of Consciousness', 'Enlarged Liver', 'Lethargy', 'Purging',
    'Bloody discharge', 'Wounds'
]

def predict_disease(symptoms_selected):
    
    example_symptoms = {}
    for i, symptom in enumerate(symptoms_selected, start=1):
        if i <= 7:  
            example_symptoms[f'Symptom_{i}_{symptom}'] = 1

    
    example_df = pd.DataFrame([example_symptoms])
    training_features = rf_model.feature_names_in_  
    example_df = example_df.reindex(columns=training_features, fill_value=0)

    
    prediction = rf_model.predict(example_df)
    
    return prediction[0]


def symptom_check(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms_selected = form.cleaned_data['symptoms']
            predicted_disease = predict_disease(symptoms_selected)
            return render(request, 'result.html', {'disease': predicted_disease})
    else:
        form = SymptomForm()

    return render(request, 'form.html', {'form': form})



from django.shortcuts import render
from django.core.files.storage import default_storage
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np


model = load_model('app\model.h5')

img_size = (150, 150)
class_names = ['flea_allergy', 'hotspot', 'mange', 'ringworm']  

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        img_path = default_storage.save('uploads/' + image.name, image)

        
        img = load_img(img_path, target_size=img_size)
        img_array = img_to_array(img) / 255.0  
        img_array = np.expand_dims(img_array, axis=0) 

       
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        predicted_disease = class_names[predicted_class]

       
        return render(request, 'res2.html', {'disease': predicted_disease})

    return render(request, 'upload.html')



from .forms import CowSymptomForm
from .ml_model import voting_clf,predict_disease_cow,X_train
import pandas as pd

def symptom_check_cow(request):
    if request.method == 'POST':
        form = CowSymptomForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data['symptoms']
            
           
            symptom_data = {symptom: 0 for symptom in X_train.columns}
            
           
            for symptom in selected_symptoms:
                symptom_data[symptom] = 1
            
           
            predicted_disease = predict_disease_cow(symptom_data)
            
            
            return render(request, 'symptom_result.html', {'predicted_disease': predicted_disease})
    else:
        form = CowSymptomForm()
    
    return render(request, 'symptom_check.html', {'form': form})
