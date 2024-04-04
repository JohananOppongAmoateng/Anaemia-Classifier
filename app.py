import gradio as gr
import joblib
import numpy as np

def preprocessing(gender):
    if gender == "Male":
        return 0
    elif gender == "Female":
        return 1
  
def predict(Gender,Haemoglobin,MCH,MCHC,MCV):
    model = joblib.load("models/svm.pkl")
    gender = preprocessing(Gender)
    data = np.array([[gender,Haemoglobin,MCH,MCHC,MCV]])
    pred = model.predict(data)
    if pred == 0:
        return "Not Anaemic"
    else:
        return "Anaemic"
    

demo = gr.Interface(
    fn=predict,
    inputs=[gr.Radio(choices=["Male","Female"],value="str",label="Gender",info="Choose Gender"),
            gr.Number(label="Haemoglobin"),
            gr.Number(label="MCH"),
            gr.Number(label="MCHC"),
            gr.Number(label="MCV"),
            ],
    outputs=["text"],
)

demo.launch()
