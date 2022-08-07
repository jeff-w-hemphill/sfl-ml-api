# Description

An API endpoint to use a neural network that classifies clothing. It was trained using Fashion MNIST data.
Public version launched on an AWS EC2 instance: http://ec2-54-166-161-90.compute-1.amazonaws.com/docs

# Model Overview

I used 70,000 images from the Fashion MNIST dataset. 60,000 were for training and 10,000 were for testing. Overall, the model performed with and accuracy of 88%.

Labels:  
1. T-shirt/Top
2. Trouser
3. Pullover
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle Boot

For more details about the model see ``classification.ipynb``` in this directory.
<br>

# API Overview

API developed using FastAPI - a python framework
<br>

## Starting the API
### Using Docker  


Build the Container
```
docker build .
```
Get image id
```
docker images
```
Run
```
docker run -d -p <port>:<port> <image_id>
```
To stop use ```docker stop <container_id>```
<br>
<br>

### Using python environment  

Install requirements
```
pip3 install -r requirements.txt
```
Start
```
uvicorn main:app --reload
```
<br>

## Endpoints

Once the application is running, navigate to ```/docs``` to view and test the endpoints.

Example:
```
http://localhost:8000/docs
```
```GET /``` -> index page. 

```POST /``` -> returns model predictions of given photo.  

```GET /docs``` -> to read about and test endpoints.

Here is an example request-response of the ```POST /``` endpoint:

#### Request
```
curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@shirt2.jpeg;type=image/jpeg'
```

#### Response
```
{
  "file_name": "shirt2.jpeg",
  "predictions": {
    "T-shirt/top": "96.08%",
    "Trouser": "0.0%",
    "Pullover": "0.05%",
    "Dress": "0.0%",
    "Coat": "0.35%",
    "Sandal": "0.0%",
    "Shirt": "2.0%",
    "Sneaker": "0.0%",
    "Bag": "1.51%",
    "Ankle boot": "0.0%"
  }
}
```