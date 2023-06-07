# Baseline bem simples com dados reduzidos
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer

from ast import literal_eval
import os
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

import tensorflow as tf

classes = ['.htaccess', '.net', 'actionscript-3', 'ajax', 'algorithm','amazon-web-services', 'android', 'android-layout','android-studio', 'angularjs', 'apache', 'api', 'arrays','asp.net', 'asp.net-mvc', 'asp.net-mvc-3', 'asp.net-mvc-4','azure', 'bash', 'batch-file', 'c', 'c#', 'c++', 'c++11', 'class','cocoa', 'cocoa-touch', 'codeigniter', 'cordova', 'css', 'css3','csv', 'database', 'date', 'datetime', 'debugging', 'delphi','django', 'eclipse', 'email', 'entity-framework', 'excel','excel-vba', 'facebook', 'file', 'flash', 'forms', 'function','git', 'google-app-engine', 'google-chrome', 'google-maps','hadoop', 'haskell', 'hibernate', 'html', 'html5', 'http', 'image','internet-explorer', 'ios', 'ipad', 'iphone', 'java', 'javascript','jquery', 'jquery-ui', 'jsf', 'json', 'jsp', 'laravel', 'linq','linux', 'list', 'listview', 'loops', 'magento', 'matlab', 'maven','mongodb', 'ms-access', 'multithreading', 'mysql', 'node.js','object', 'objective-c', 'oop', 'opencv', 'oracle', 'osx','pandas', 'parsing', 'performance', 'perl', 'php', 'pointers','postgresql', 'powershell', 'python', 'python-2.7', 'python-3.x','qt', 'r', 'regex', 'rest', 'ruby', 'ruby-on-rails','ruby-on-rails-3', 'ruby-on-rails-4', 'scala', 'security','selenium', 'session', 'shell', 'sockets', 'sorting', 'spring','spring-mvc', 'sql', 'sql-server', 'sql-server-2008', 'sqlite','string', 'swift', 'swing', 'symfony2', 'templates', 'tomcat','tsql', 'twitter-bootstrap', 'ubuntu', 'uitableview','unit-testing', 'unix', 'user-interface', 'validation','variables', 'vb.net', 'vba', 'visual-studio','visual-studio-2010', 'wcf', 'web-services', 'windows', 'winforms','wordpress', 'wpf', 'xaml', 'xcode', 'xml']

with open('app/models/baseline_modelv1.pkl','rb') as f:
    pipeline = pickle.load(f)  
    
# print(pipeline.predict_proba(["""31

# I was looking for a tutorial on how to install Python libraries in the wheel format.

# It does not seem straightforward so I'd appreciate a simple step by step tutorial how to install the module named "requests" for CPython.

# I downloaded it from: https://pypi.python.org/pypi/requests and now I have a .whl file. I've got Python 2.7 and 3.3 on Windows, so how do I install it so all the other Python scripts I run can use it?"""]))

CLF = tf.keras.saving.load_model("app/models/inhouse")

s = CLF.predict(["""31

I was looking for a tutorial on how to install Python libraries in the wheel format.

It does not seem straightforward so I'd appreciate a simple step by step tutorial how to install the module named "requests" for CPython.

I downloaded it from: https://pypi.python.org/pypi/requests and now I have a .whl file. I've got Python 2.7 and 3.3 on Windows, so how do I install it so all the other Python scripts I run can use it?"""])

print(s)
