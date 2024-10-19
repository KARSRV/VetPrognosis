from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(label='', max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Type your question...'}))

from django import forms


SYMPTOMS = [
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

class SymptomForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        choices=[(symptom, symptom) for symptom in SYMPTOMS],
        widget=forms.CheckboxSelectMultiple,
        label="Select Symptoms"
    )

    
    def __init__(self, *args, **kwargs):
        super(SymptomForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'custom-checkbox',
            })

class ImageUploadForm(forms.Form):
    image = forms.ImageField()            

from django import forms


SYMPTOMS = [
    'anorexia', 'abdominal_pain', 'anaemia', 'abortions', 'acetone', 'aggression',
    'arthrogyposis', 'ankylosis', 'anxiety', 'bellowing', 'blood_loss', 'blood_poisoning',
    'blisters', 'colic', 'Condemnation_of_livers', 'conjunctivae', 'coughing', 'depression',
    'discomfort', 'dyspnea', 'dysentery', 'diarrhoea', 'dehydration', 'drooling', 'dull',
    'decreased_fertility', 'diffculty_breath', 'emaciation', 'encephalitis', 'fever',
    'facial_paralysis', 'frothing_of_mouth', 'frothing', 'gaseous_stomach', 'highly_diarrhoea',
    'high_pulse_rate', 'high_temp', 'high_proportion', 'hyperaemia', 'hydrocephalus',
    'isolation_from_herd', 'infertility', 'intermittent_fever', 'jaundice', 'ketosis',
    'loss_of_appetite', 'lameness', 'lack_of-coordination', 'lethargy', 'lacrimation',
    'milk_flakes', 'milk_watery', 'milk_clots', 'mild_diarrhoea', 'moaning', 'mucosal_lesions',
    'milk_fever', 'nausea', 'nasel_discharges', 'oedema', 'pain', 'painful_tongue', 'pneumonia',
    'photo_sensitization', 'quivering_lips', 'reduction_milk_vields', 'rapid_breathing',
    'rumenstasis', 'reduced_rumination', 'reduced_fertility', 'reduced_fat', 'reduces_feed_intake',
    'raised_breathing', 'stomach_pain', 'salivation', 'stillbirths', 'shallow_breathing',
    'swollen_pharyngeal', 'swelling', 'saliva', 'swollen_tongue', 'tachycardia', 'torticollis',
    'udder_swelling', 'udder_heat', 'udder_hardeness', 'udder_redness', 'udder_pain',
    'unwillingness_to_move', 'ulcers', 'vomiting', 'weight_loss', 'weakness', 'prognosis'
]

class CowSymptomForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        choices=[(symptom, symptom) for symptom in SYMPTOMS],
        widget=forms.CheckboxSelectMultiple,
        label="Select the symptoms your cow is experiencing:"
    )
    
    
    def __init__(self, *args, **kwargs):
        super(CowSymptomForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'custom-checkbox',
            })
