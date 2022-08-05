from fastapi import FastAPI, UploadFile, File
from utils import imageprepare
import pickle
import shutil
from fastapi.responses import JSONResponse
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def predict_clothing(file: UploadFile = File(...)):
    # validate file type is jpg, jpeg, or png
    if file.content_type not in ('image/jpg', 'image/jpeg', 'image/png'):
        return { "Error": "File must be jpg, jpeg, or png format."}
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    prepared_image = imageprepare(file.filename)
    pickled_model = 'fashion_prediction_model'
    model = pickle.load(open(pickled_model, 'rb'))
    prediction = model.predict(prepared_image)
    
    os.remove(file.filename)
    
    # create dictionary obj to send
    prediction = prediction[0].tolist() 
    labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    label_map = {}
    
    for i, p in enumerate(prediction):
        label_map[labels[i]] = str(round(p * 100, 2)) + '%'
    
    return JSONResponse({"file_name": file.filename, "predictions": label_map})
