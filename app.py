import gradio as gr
import pickle
import numpy as np
import pandas as pd

# load
with open('finalinsurance.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_gpa(age, sex, bmi, children, smoker, region):
    columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

    inputDF = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
        columns=columns)

    # The model may expect specific dtypes/encodings for categorical columns.
    # Make sure the DataFrame column names and order match what the model was trained on.
    prediction = model.predict(inputDF)[0]

    # return a plain Python float clipped to the expected GPA range
    return prediction

inputs = [


    gr.Number(label = 'Age', value = 18),
    gr.Radio(["male", "female"], label = "Gender"),
    gr.Number(label='BMI', value = 24),
    gr.Slider(0, 4, step = 1, label='Children'),
    gr.Radio(['yes', 'no'], label='Smoker'),
    gr.Dropdown(['southwest', 'northwest', 'southeast', 'northeast'], label = 'Region'),
 

    


]   
#

# interface
app = gr.Interface(
    fn = predict_gpa,
    inputs=inputs,
    outputs=gr.Number(label='Predicted Insurance Cost: '),
    title='Insurance Cost Predictor'
)

#launch
app.launch()