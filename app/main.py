from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import tensorflow as tf
import re
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

CLASSES = ['.htaccess', '.net', 'actionscript-3', 'ajax', 'algorithm','amazon-web-services', 'android', 'android-layout','android-studio', 'angularjs', 'apache', 'api', 'arrays','asp.net', 'asp.net-mvc', 'asp.net-mvc-3', 'asp.net-mvc-4','azure', 'bash', 'batch-file', 'c', 'c#', 'c++', 'c++11', 'class','cocoa', 'cocoa-touch', 'codeigniter', 'cordova', 'css', 'css3','csv', 'database', 'date', 'datetime', 'debugging', 'delphi','django', 'eclipse', 'email', 'entity-framework', 'excel','excel-vba', 'facebook', 'file', 'flash', 'forms', 'function','git', 'google-app-engine', 'google-chrome', 'google-maps','hadoop', 'haskell', 'hibernate', 'html', 'html5', 'http', 'image','internet-explorer', 'ios', 'ipad', 'iphone', 'java', 'javascript','jquery', 'jquery-ui', 'jsf', 'json', 'jsp', 'laravel', 'linq','linux', 'list', 'listview', 'loops', 'magento', 'matlab', 'maven','mongodb', 'ms-access', 'multithreading', 'mysql', 'node.js','object', 'objective-c', 'oop', 'opencv', 'oracle', 'osx','pandas', 'parsing', 'performance', 'perl', 'php', 'pointers','postgresql', 'powershell', 'python', 'python-2.7', 'python-3.x','qt', 'r', 'regex', 'rest', 'ruby', 'ruby-on-rails','ruby-on-rails-3', 'ruby-on-rails-4', 'scala', 'security','selenium', 'session', 'shell', 'sockets', 'sorting', 'spring','spring-mvc', 'sql', 'sql-server', 'sql-server-2008', 'sqlite','string', 'swift', 'swing', 'symfony2', 'templates', 'tomcat','tsql', 'twitter-bootstrap', 'ubuntu', 'uitableview','unit-testing', 'unix', 'user-interface', 'validation','variables', 'vb.net', 'vba', 'visual-studio','visual-studio-2010', 'wcf', 'web-services', 'windows', 'winforms','wordpress', 'wpf', 'xaml', 'xcode', 'xml']

with open('models/baseline_modelv1.pkl','rb') as f:
    baseline = pickle.load(f)
    
inhouse = tf.keras.saving.load_model("models/inhouse")

def clean_body(txt:str):
    new = re.sub("[^0-9a-zA-Z]+"," ",txt)
    return new

def predict_baseline(text : str):
    new = clean_body(text)
    prediction = baseline.predict_proba([new])
    print(prediction)
    top_3_labels = [
        x
        for _, x in sorted(
            zip(prediction[0,:], CLASSES),
            key=lambda pair: pair[0],
            reverse=True,
        )
    ][:3]

    return top_3_labels

def predict_inhouse(text : str):
    new = clean_body(text)
    prediction = inhouse.predict([new])
    print(prediction)
    top_3_labels = [
        x
        for _, x in sorted(
            zip(prediction[0,:], CLASSES),
            key=lambda pair: pair[0],
            reverse=True,
        )
    ][:3]
    return top_3_labels

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to the specific origin(s) you want to allow
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": "v2"}

@app.get("/baseline/{input_string}")
def prediction(input_string: str):
    language = " , ".join(predict_baseline(input_string))
    return {"Tags": language}

@app.get("/inhouse/{input_string}")
def predict(input_string: str):
    language = " , ".join(predict_inhouse(input_string))
    return {"Tags": language}