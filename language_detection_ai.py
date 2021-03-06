# -*- coding: utf-8 -*-
"""Language Detection AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M84j6fsBL91J24AT0rPBLsi4bSNInszw

> # Language Detection Artificial Intelligence Software - By Prateek Dutta

It is an NLP system. The sensitivity score is quite high and the accuracy score is in a very advantageous position. It has 97% accuracy score. I have shared Dataset and Artificial Intelligence Software as open source. I have used the Ridge Classifier algorithm and manipulated the dataset to improve the algorithm. In this way, the sensitivity rate and score of the software has been increased. In addition, I adapted the data according to the algorithm and made the algorithm work. In this study, it was studied on the data, not on the algorithm.


###**The coding language used:**

`Python 3.9.8`

###**Libraries Used:**

`NumPy`

`Pandas`

`Scikit-learn (SKLEARN)`
     
### **Creator Information:**

Name-Surname: **Prateek Dutta**

Contact (Email) : **prateekdutta2001@gmail.com**

LinkedIn : **[https://www.linkedin.com/in/prateek-dutta-3622821a1/][LinkedinAccount]**

[LinkedinAccount]: https://www.linkedin.com/in/prateek-dutta-3622821a1/


Official Website: **[https://prateekduttaportfolio.wordpress.com/][OfficialWebSite]**

[OfficialWebSite]: https://prateekduttaportfolio.wordpress.com/
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive/')
# %cd /gdrive

ls

cd/gdrive/MyDrive/Language Detection/

ls

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

data = pd.read_csv('/gdrive/MyDrive/Language Detection/language_detection.csv')
data.head(5)

"""### Value Counts of Language Label"""

data["language"].value_counts()

"""### Value Counts of Text Feature"""

data["Text"].value_counts()

"""> # *Process*
> * **Import to ML (scikit-learn) Libraries**
> * **Data Preprocessing**
> * **NLP system entegration to Data**
> * **Model Creating**
"""

#Import to ML (scikit-learn) Libraries
from sklearn.linear_model import RidgeClassifier #RidgeClassifier

#Data Preprocessing
X_train, X_test, y_train, y_test = train_test_split(data.Text, 
                                                    data.language,
                                                    test_size=0.325000000000000001,
                                                    random_state=2551,
                                                    shuffle=True)
#NLP system entegration to Data    
X_CountVectorizer = CountVectorizer(stop_words='english')

X_train_counts = X_CountVectorizer.fit_transform(X_train)

X_TfidfTransformer = TfidfTransformer()

X_train_tfidf = X_TfidfTransformer.fit_transform(X_train_counts)

#Model Creating
model = RidgeClassifier()

model.fit(X_train_tfidf, y_train)

"""> # *Model Accuracy Score*
> * **model.score([Test_data])**
"""

model.score(X_CountVectorizer.transform(X_test),y_test)

"""> # *Prediction*"""

#Data of Prediction
text = """Myself Prateek Dutta. I am an Author & Research scholar from India pursuing B.Tech in Artificial Intelligence. """

text = [text]

text_counts = X_CountVectorizer.transform(text)

#Prediction Processing
prediction = model.predict(text_counts)

f"Prediction is {prediction[0]}"

#Data of Prediction
text = """Kendim Prateek Dutta. Yapay Zeka alan??nda B.Tech'i takip eden Hindistan'dan bir Yazar ve Ara??t??rma bilginiyim."""

text = [text]

text_counts = X_CountVectorizer.transform(text)

#Prediction Processing
prediction = model.predict(text_counts)

f"Prediction is {prediction[0]}"

